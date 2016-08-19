import thriftpy

logger_service = thriftpy.load("../LoggerService.thrift", "loggerservice_thrift")

from thriftpy.rpc import make_client

client = make_client(logger_service.Logger, '127.0.0.1', 9090)

logfile = "logfile.log"
client.timestamp(logfile)
print ("Logged timestamp to log file")
                
client.write_log(logfile, "This is a message that I am writing to the log")
client.timestamp(logfile)

print ("Last line of log file is: %s" % (client.get_last_log_entry(logfile)))
print ("Size of log file is: %d bytes" % client.get_log_size(logfile))
