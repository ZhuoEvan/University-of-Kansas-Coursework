// quash_listener.cpp
/*
 *
 *
 *
 *
 */

//Imported C++ Libraries
#include "quash_func.h"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

//Imported C Libraries
#include <cstdlib>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

//Shorten C++ Methods
using namespace std;

//Global Variables
int key;

//External Command Execution # Used ChatGPT for function
void exec_xcmd(vector<string> args, int input_fd, int output_fd, bool wait_c) {
    //Local Variables
    bool background = false;
    
    if ((args.size() != 0) && args.back() == "&") {
        background = true;
        args.pop_back();
        wait_c = false;
    }

    pid_t pid = fork();

    if (pid == -1) return;
    if (pid == 0) { //Child Process
        if (input_fd != STDIN_FILENO) {
            dup2(input_fd, STDIN_FILENO);
            close(input_fd);
        }
        if (output_fd != STDOUT_FILENO) {
            dup2(output_fd, STDOUT_FILENO);
            close(output_fd);
        }
        vector<char*> argv;
        for (const auto& arg: args) {
            argv.push_back(const_cast<char*>(arg.c_str()));
        }
        argv.push_back(nullptr);

        execvp(argv[0], argv.data());
        perror("execvp");
        exit(EXIT_FAILURE);
    } else { //Parent Process
        if (background) {
            string arg_str;
            for (const auto& arg : args) {
                arg_str += arg + " ";
            }
            arg_str += "&";
            add_background_job(pid, arg_str);
            return;
        } else if (wait_c) {
            waitpid(pid, nullptr, 0);
            return;
        }
    }
    return;
}

/* Pipe Helper Functions
 * These helper functions are used to implement pipes
 * into Quash.
 * # Used ChatGPT for help.
 */
bool pipe_exist(vector<string> args) {
    for (unsigned long i = 0; i < args.size(); i++) {
        if (args[i] == "|") return true;
    }
    return false;
}

vector<vector<string>> pipe_split(vector<string> args) {
    //Local Variables
    vector<vector<string>> pipe_args;
    vector<string> current_arg;

    for (unsigned long i = 0; i < args.size(); i++) {
        if (args[i] == "|") {
            if (!(current_arg.empty())) {
                pipe_args.push_back(current_arg);
                current_arg.clear();
            }
        } else {
            current_arg.push_back(args[i]);
        }
    }
    if (!(current_arg.empty())) {
        pipe_args.push_back(current_arg);
    }
    return pipe_args;
}

void pipeline_read(vector<vector<string>> pipe_args) {
    //Error Check: Segmentation Fault
    if (pipe_args.size() == 0) return;

    //Background Process Handler
    bool background = false;

    if (pipe_args.size() != 0 && pipe_args.back().back() == "&") {
        background = true;
        pipe_args.back().pop_back();

        if(pipe_args.back().empty()) {
            pipe_args.pop_back();
        }
    }

    vector<pid_t> pids;
    vector<vector<int>> pipes(pipe_args.size() - 1, vector<int>(2));

    for (unsigned long i = 0; i < pipe_args.size() - 1; i++) {
        if (pipe(pipes[i].data()) == -1) {
            perror("pipe");
            return;
        }
    }

    for (unsigned long j = 0; j < pipe_args.size(); j++) {
        pid_t pid = fork();

        if (pid == -1) {
            perror("fork");
            return;
        }

        if (pid == 0) { //Child Process
            if (j > 0) dup2(pipes[j - 1][0], STDIN_FILENO);
            if (j < pipe_args.size() - 1) dup2(pipes[j][1], STDOUT_FILENO);
            for (unsigned long k = 0; k < pipe_args.size() - 1; k++) {
                close(pipes[k][0]);
                close(pipes[k][1]);
            }

            //
            string p_arg = pipe_args[j][0];
            bool quash_func = false;

            if (p_arg == "echo") {
                echo(pipe_args[j]);
                quash_func = true;
            } else if (p_arg == "pwd") {
                pwd();
                quash_func = true;
            } else if (p_arg == "ls") {
                ls(pipe_args[j]);
                quash_func = true;
            }

            //External Command # Used ChatGPT for external command
            if (!(quash_func)) {
                vector<char*> argv;
                for (const auto& arg: pipe_args[j]) {
                    argv.push_back(const_cast<char*>(arg.c_str()));
                }
                argv.push_back(nullptr);

                //Execute External Command
                execvp(argv[0], argv.data());
                perror("execvp");
            }
            exit(EXIT_FAILURE);
        } else pids.push_back(pid); // Parent Process
    }

    //Close File Descriptors in Parent Process
    for (unsigned long i = 0; i < pipe_args.size() - 1; i++) {
        close(pipes[i][0]);
        close(pipes[i][1]);
    }

    if (background) {
        string arg_str;
        for (const auto& args : pipe_args) {
            for (const auto& arg : args) {
                arg_str += arg + " ";
            }
            arg_str += "| ";
        }
        if (arg_str.size() != 0) {
            arg_str = arg_str.substr(0, arg_str.length() - 3);
            arg_str += "&";
        }
    }

    //Child Process Wait
    for (pid_t pid : pids) {
        waitpid(pid, nullptr, 0);
    }
    return;
}

//Argument to Integer Converter Function
int arg_to_int(string s) {
    vector<string> arg_list = {"echo", "export", "cd", 
                                "pwd", "quit", "exit", 
                                "jobs", "kill", "help",
                                "&", "ls", "|"};

    for (unsigned long i = 0; i < arg_list.size(); i++) {
        if (s == arg_list[i]) return i + 1;
    }
    return 63;
}

//Argument Reader Function {TRUE = QUIT | FALSE = CONTINUE}
bool arg_read(vector<string> args) {
    //Error Check: Segmentation Fault
    if (args.size() == 0) return false;

    //Pipe Check
    if (pipe_exist(args)) {
        vector<vector<string>> pipe_args = pipe_split(args);
        pipeline_read(pipe_args);
        return false;
    }

    //Convert argument into integer to use switch
    key = arg_to_int(args[0]);

    //Function Call Switch
    switch(key) {
        case 1: //echo Call
            echo(args);
            return false;
        case 2: //export Call
            evanport(args);
            return false;
        case 3: //cd Call
            cd(args);
            return false;
        case 4: //pwd Call
            pwd();
            return false;
        case 5: //quit Call
            if (args.size() == 1) return true;
        case 6: //exit Call
            if (args.size() == 1) return true;
        case 7: //jobs Call
            jobs();
            return false;
        case 8: //kill Call
            kill(args);
            return false;
        case 10: //& Call
            return false;
        case 11: //ls Call
            ls(args);
            return false;
        default:
            exec_xcmd(args, STDIN_FILENO, STDOUT_FILENO, true);
            return false;
    }

    return false;
}

//Fill Environment Variable Function
vector<string> fill_env(vector<string> v) {

    for (unsigned long i = 0; i < v.size(); i++) {
        if (!(v[i].empty()) && v[i][0] == '$') {
            string env_var = v[i].substr(1);
            const char* path_value = getenv(env_var.c_str());

            if (path_value != nullptr) {
                v[i] = path_value;
            } else {
                cout << "No path value" << endl;
            }
        }
    }
    return v;
}

//Filter Quote Function
vector<string> filter_quote(vector<string> v) {
    unsigned long i;
    for (i = 0; i < v.size(); i++) {
        string s = v[i];
        s.erase(remove(s.begin(), s.end(), '\"'), s.end());
        s.erase(remove(s.begin(), s.end(), '\''), s.end());
        v[i] = s;
    }
    return v;
}

//Filter Comment Function
vector<string> filter_comment(vector<string> v) {
    //Local Variables
    bool detected = false;
    bool found = false;
    unsigned long i;
    unsigned long j;

    /* Find # (Comment) in Vector 
     * Accessing all strings in the vector. Accessing all char in strings.
     */
    for (i = 0; i < v.size(); i++) {
        for (j = 0; j < v[i].size(); j++) {
            if (v[i][j] == '#') {
                detected = true;
                break; //Early Termination Part 1
            }
        }
        if (detected) break; //Early Termination Part 2
    }

    //Filter Comments from Command
    if (detected) {
        vector<string> f_v; //Create Filter Vector
        
        for (i = 0; i < v.size(); i++) {
            if (v[i][0] == '#') {
                found = true;
                break;
            }
            if (found) break;
            f_v.push_back(v[i]);
        }
        return f_v;
    }
    return v; 
}

//Filter Function
vector<string> filter(vector<string> v) {
    v = filter_comment(v); //Comment Filter
    v = filter_quote(v); //Quote Filter
    v = fill_env(v); //Fill Environment Variable
    return v;
}

//Split String Function
vector<string> split(const string s, char space) {
    //Local Variables
    vector<string> tokens;
    string token;
    istringstream token_stream(s);

    //Fill tokens Vector with token
    while (getline(token_stream, token, space)) {
        tokens.push_back(token);
    }

    return tokens;
}

//Argument Listener System
void listener(bool b) {
    //Local Variables
    vector<string> args;
    vector<string> f_args;
    string raw_arg;

    while (b) {
        //Check on Job
        update_job();

        //Waiting for Input
        cout << "[sQUASH]$ "; getline(cin, raw_arg);

        //Clean Up Input
        args = split(raw_arg, ' ');
        f_args = filter(args);
        b = !(arg_read(f_args));
    }
    //Quash Termination  
    return;
}

