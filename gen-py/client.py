import sys
sys.path.append('gen-py')


from LoggerPy import Logger

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
        # Make socket
        transport = TSocket.TSocket('localhost', 9090)

        # Buffering is critical. Raw sockets are very slow
        transport = TTransport.TBufferedTransport(transport)

        # Wrap in a protocol
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        client = Logger.Client(protocol)
        transport.open()

        logfile="logfile.log"

        client.timestamp(logfile)
        print ("Logged timestamp to log file")
        
        client.write_log(logfile, "This is a message that I am writing to the log")
        client.timestamp(logfile)
        print ("Last line of log file is: %s" % (client.get_last_log_entry(logfile)))
        print ("Size of log file is: %d bytes" % client.get_log_size(logfile))

        transport.close()

except TTransport.TTransportException:
    print ("Error starting client")

except Thrift.TApplicationException, e:
    print ("%s" % (e))

except Thrift.TException, e:
    print ("Error: %d %s" % (e.error_code, e.error_description))
