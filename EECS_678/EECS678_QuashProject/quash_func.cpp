// quash_func.cpp

//Imported C++ Libraries
#include "quash_func.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <filesystem>
#include <unordered_map>
#include <atomic>

//Imported C Libraries
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>

//Shorten C++ Methods
using namespace std;

//Aesthetic Definitions
#define BLUE    "\033[34m"
#define YELLOW  "\033[33m" 
#define RESET   "\033[0m"

/* Job Main # Used ChatGPT for Job helper functions
 * add_background_job() | update_job()
 */

//Job Global Variables
vector<Job> job_list;
atomic<int> next_jobid{1};

//Job Functions
void add_background_job(pid_t pid, string arg) {
    //Create Job Structure
    Job new_job;

    //Fill in Job Structure
    new_job.job_id = next_jobid++;
    new_job.pid = pid;
    new_job.arg = arg;
    new_job.completed = false;

    job_list.push_back(new_job);
    cout << "Background job started: [" << new_job.job_id << "] " << pid << ' ' <<
    arg << endl;
    return;
}

void update_job() {
    for (unsigned long i = 0; i < job_list.size(); i++) {
        if (!(job_list[i].completed)) {
            int status;
            pid_t result = waitpid(job_list[i].pid, &status, WNOHANG);

            if (result > 0) {
                job_list[i].completed = true;
                cout << "Completed: [" << job_list[i].job_id << "] " << job_list[i].pid << ' ' <<
                job_list[i].arg << endl;
            }
        }
    }
    //Remove Job from job_list # Used ChatGPT
    job_list.erase(remove_if(job_list.begin(), job_list.end(), [](const Job& job) 
    { return job.completed; }), job_list.end());
    return;
}

/* Helper Functions
 * find_str() | locate_str() | write_to_file() | read_from_file() | append_to_file()
 * find_path() |
 */
 bool find_str(vector<string> v, string search_str) {
    for (unsigned long i = 1; i < v.size(); i++) {
        if (v[i].find(search_str) != string::npos) return true;
    }
    return false;
 }

 void write_to_file(vector<string> v, string file_name) {
    ofstream my_file(file_name);

    return;
 }

 void read_from_file(vector<string> v, string file_name) {
    ifstream my_file(file_name);

    return;
 }

string find_path(vector<string> args) {
    return args[1];
}


/* Built-in Functions
 * echo()
 * export() (evanport())
 * cd()
 * pwd()
 * jobs()
 * kill()
 * ls()
 */
//echo Function
void echo(vector<string> args) {
    //Local Variables
    bool write = find_str(args, ">");
    bool read = find_str(args, "<");
    // bool append = find_str(args, ">>");
    vector<unsigned long> str_pos;

    //Error Check: Segmentation Fault
    if (args.size() < 2) {
        cout << endl;
        return;
    }

    //Specify Echo Block
    if (write && read) { //echo (read & write)
        cout << "read & write" << endl;
    } else if (read) { //echo (read only)
        cout << "read only" << endl;
    } else if (write) { //echo (write only)
        cout << "write only" << endl;
    } else { //echo (no write or read)
        for (unsigned long i = 1; i < args.size(); i++) {
            cout << args[i] << ' ';
        }
        cout << endl;
    }

    return;
}

//export Function
void evanport(vector<string> args) {
    if (args.size() != 2) {
        cout << "Invalid" << endl;
        return;
    }

    char* env_var = strdup(args[1].c_str());
    if (putenv(env_var) == 0) {
        return;
    } else free(env_var);
    return;
}

//cd Function
void cd(vector<string> args) {
    if (args.size() < 2) {
        filesystem::current_path().root_path();
        return;
    }

    if (args.size() > 2) {
        cout << "Too many arguments" << endl;
        return;
    }

    string path = find_path(args);

    try {
        filesystem::current_path(path);
    } catch (const filesystem::filesystem_error& e) {
        cout << "Invalid Path" << endl;
    }
    
    return;
}

//pwd Function
void pwd() {
    filesystem::path c = filesystem::current_path();
    cout << c << endl;
    return;
}

//jobs Function
void jobs() {
    //Check Job Update
    update_job();

    //No Jobs in job_list
    if (job_list.size() == 0) return;

    //List All Jobs
    for (unsigned long i = 0; i < job_list.size(); i++) {
        if (!(job_list[i].completed)) {
            cout << "[" << job_list[i].job_id << "] " << job_list[i].pid << " " <<
            job_list[i].arg << endl;
        }
    }
    return;
}

//kill Function
void kill(vector<string> args) {
    //Error Check: Segmentation Fault
    if (args.size() < 3) {
        cout << "Too few arguments" << endl;
        return;
    }

    int signal_num = stoi(args[1]);
    int job_id = stoi(args[2]);

    //Error Check: SIGNUM in range
    if (signal_num < 1 || signal_num > 31) {
        cout << "Invalid SIGNUM" << endl;
        return;
    }

    for (unsigned long i = 0; i < job_list.size(); i++) {
        if (job_list[i].job_id == job_id && !(job_list[i].completed)) {
            job_list[i].completed = true;
            return;
        }
    }
    cout << "Job [" << job_id << "] was not found" << endl;
    return;
}

//ls Function   # Used stackOverflow
void ls(vector<string> args) {
    //Local Variables
    filesystem::path fp = filesystem::current_path();

    //Base ls Function
    if (args.size() == 1) {
        for (const auto& entry : filesystem::directory_iterator(fp)) {
            if (entry.path().filename().string()[0] != '.') {
                cout << BLUE << entry.path().filename().string() << RESET << ' '; // # Used ChatGPT for color
            }
        }
        cout << endl;
        return;

    //Special ls Function
    } else {
        //Local Variables
        vector<string> files_vector;
        bool weak_hidden = false;
        bool hidden = false;
        bool show_long = false;

        //Read flags
        for (unsigned long i = 1; i < args.size(); i++) {
            if ((!(args[i].empty()) && args[i][0] == '-' && args[i].size() == 2) || args[i][0] == '/') {
                if (args[i][0] == '/') {
                    fp = filesystem::current_path().root_path();
                } else if (args[i][1] == 'a') hidden = true;
                else if (args[i][1] == 'A') weak_hidden = true;
                else if (args[i][1] == 'l') show_long = true;
                
            } else {
                cout << YELLOW << "The flag " << RESET <<
                args[i] << YELLOW << " is invalid" << RESET << endl;
                return;
            }   
        }

        //Push Current and Parent Directory for -a
        if (hidden && !(weak_hidden)) {
            files_vector.push_back(".");
            files_vector.push_back("..");
        }
        
        //Toggle Hidden for Weak Hidden
        if (weak_hidden) hidden = true;

        for (const auto& entry : filesystem::directory_iterator(fp)) {
            if (!(hidden) && entry.path().filename().string()[0] == '.') continue;

            if (show_long) files_vector.push_back(entry.path().string());
            else files_vector.push_back(entry.path().filename().string());
             // entry.path().filename().string()
        }

        for (unsigned long j = 0; j < files_vector.size(); j++) {
            cout << BLUE << files_vector[j] << RESET << ' ';
        }
        cout << endl;
        return;
    }
    return;
}
