#include <iostream>

#include "Logger.h"

#include <thrift/transport/TSocket.h>
#include <thrift/transport/TBufferTransports.h>
#include <thrift/protocol/TBinaryProtocol.h>

using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;

using namespace LoggerCpp;

int main(int argc, char **argv) 
{
    char logfile[]="logfile.log";
    std::string line;

    boost::shared_ptr<TSocket> socket(new TSocket("localhost", 9090));
    boost::shared_ptr<TTransport> transport(new TBufferedTransport(socket));
    boost::shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));

    LoggerClient client(protocol);
    
    try
    {
    
        transport->open();
    
        client.timestamp(logfile);
        std::cout << "Logged timestamp to log file" << std::endl;

        client.write_log(logfile, "This is a message that I am writing to the log");
        client.timestamp(logfile);

        client.get_last_log_entry(line, logfile);
        std::cout << "Last line of the log file is: " << line << std::endl;
        std::cout << "Size of log file is: " << client.get_log_size(logfile) << " bytes" << std::endl;

        transport->close();
    }

    catch (TTransportException e)
    {
        std::cout << "Error starting client" << std::endl;
    }

    catch (LoggerException e)
    {
        std::cout << e.error_description << std::endl;
    }
    
    return 0;
}
