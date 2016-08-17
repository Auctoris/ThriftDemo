cmake_minimum_required(VERSION 3.5)

project(LoggerService)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall -DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H")

set(THRIFT_DIR "/usr/local/include/thrift")
set(BOOST_DIR "/usr/local/Cellar/boost/1.60.0_2/include/")

include_directories(${THRIFT_DIR} ${BOOST_DIR} ${CMAKE_SOURCE_DIR})
link_directories(/usr/local/lib)

set(BASE_SOURCE_FILES Logger.cpp LoggerService_types.cpp LoggerService_constants.cpp)
set(SERVER_FILES LoggerServer.cpp)
set(CLIENT_FILES LoggerClient.cpp)

add_executable(LoggerServer ${SERVER_FILES} ${BASE_SOURCE_FILES})
add_executable(LoggerClient ${CLIENT_FILES} ${BASE_SOURCE_FILES})

target_link_libraries(LoggerServer thrift)
target_link_libraries(LoggerClient thrift)
