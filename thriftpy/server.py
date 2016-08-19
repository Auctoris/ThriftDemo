from __future__ import print_function
import os
import datetime

import thriftpy
logger_service = thriftpy.load("../LoggerService.thrift", module_name="LoggerService_thrift")

from thriftpy.rpc import make_server

class Dispatcher(object):
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

server = make_server(logger_service.Logger, Dispatcher(), '127.0.0.1', 9090)
server.serve()
