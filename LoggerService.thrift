namespace py LoggerPy
namespace cpp LoggerCpp

exception LoggerException
{
    1: i32 error_code,
    2: string error_description
}

service Logger
{
    oneway void timestamp (1: string filename)
    string get_last_log_entry (1: string filename) throws (1: LoggerException error)
    void write_log (1: string filename, 2: string message) throws (1: LoggerException error)
    i32 get_log_size (1: string filename) throws (1: LoggerException error)
}

