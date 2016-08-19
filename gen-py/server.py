from __future__ import print_function
import sys
import os
sys.path.append('gen-py')

from LoggerPy import Logger
from LoggerPy.ttypes import *
from LoggerPy.constants import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import datetime

class LoggerHandler (Logger.Iface):
    def __init__(self):
        # Initialization...
        pass

    def timestamp(self, filename):
        try:
            with open (filename, 'a') as f:
                print(datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"), file=f)
                f.close()
        except IOError as e:
            err = LoggerException()
            err.error_code = 1 
            err.error_description = "Could not open file " + filename
            raise err

    def get_last_log_entry(self, filename):
        try:
            with open (filename, 'r') as f:
                last = None
                for last in (line for line in f if line.rstrip('\n')):
                    pass

                f.close()
                return last.rstrip('\n')

        except IOError as e:
            err = LoggerException()
            err.error_code = 1 
            err.error_description = "Could not open file " + filename
            raise err

    def write_log(self, filename, message):
        try:
            with open (filename, 'a') as f:
                print(message, file=f)
                f.close()
        except IOError as e:
            err = LoggerException()
            err.error_code = 1 
            err.error_description = "Could not open file " + filename
            raise err
    
    def get_log_size(self, filename):
        return os.path.getsize(filename)

handler = LoggerHandler()
processor = Logger.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

server.serve()
