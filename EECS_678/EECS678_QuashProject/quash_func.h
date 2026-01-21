// quash_func.h
/* Header File for quash_func.cpp */

//
#ifndef QUASH_FUNC_H
#define QUASH_FUNC_H

//Import C++ Libraries
#include <string>
#include <vector>
#include <unordered_map>

//Import C Libraries
#include <sys/types.h>
#include <unistd.h>

//Job Structure
struct Job {
    int job_id;
    pid_t pid;
    std::string arg;
    bool completed;
};

//Job Functions
void add_background_job(pid_t pid, std::string arg);
void update_job();

//quash_func.cpp Imported Functions
void echo(std::vector<std::string> args);
void evanport(std::vector<std::string> args);
void cd(std::vector<std::string> args);
void pwd();
void jobs();
void kill(std::vector<std::string> args);
void ls(std::vector<std::string> args);

#endif // QUASH_FUNC_H