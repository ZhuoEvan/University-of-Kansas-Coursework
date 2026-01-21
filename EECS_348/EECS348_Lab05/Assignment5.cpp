/*
Title: EECS 348 Assignment 5
Description: Email Priority System in C++
Inputs: Assignment5_Test_File.txt
Output: Email Information and Number of Unread Emails
Collaborators: w3schools.com | stackOverflow | geeksforgeeks | Google Gemini
Name: Evan Zhuo
Date: 03/22/25
Assignment5.cpp
*/

#include <iostream> //Allow input output streams
#include <fstream> //Allow file manipulation | Used w3schools.com
#include <string> //Allow strings
#include <vector> //Allow vectors | Used stackOverflow
#include <sstream> // For istringstream

//Email Class | Created by Me
class Email {
    private: //Hidden information
        int priorityNumber; //Integer variable for priority number
    
    public: //Unhidden information
        std::string sender; //Character variable for sender information
        std::string subject; //Character variable for subject information
        std::string date; //Character variable for date information

        //Email Constructor | Used Google Gemini to fix
        Email(std::string senderInfo, std::string subjectInfo, std::string dateInfo, int priority)
            : sender(senderInfo), subject(subjectInfo), date(dateInfo), priorityNumber(priority) {} //Assign variable to information

        //Email Destructor
        ~Email() {};

        //Greater Than Operation | Used Google Gemini
        bool operator>(const Email& other) const {
            return priorityNumber > other.priorityNumber; //Compare priorityNumber
        }
};

//PriorityQueue Class | Used Google Gemini
class PriorityQueue {
    private: //Hidden Information
        std::vector<Email> priorityQueue; //Vector to store Emails

        //swap Function | Used Google Gemini to fix
        void swap(Email& a, Email& b) {
            Email temp = a; //Temporary Variable to store Email
            a = b; //Change Email a to Email b
            b = temp; //Change Email b to Email a from temporary variable
        }

        //Downheap Function | Used Google Gemini to fix
        void downHeap(int index) {
            //Initial Variables
            int leftChild = (index * 2) + 1; //leftChild expression
            int rightChild = (index * 2) + 2; //rightChild expression
            int max = index; //Variable to store largest index

            //Check if a leftChild exists and is larger than current index
            if (leftChild < priorityQueue.size() && priorityQueue[leftChild] > priorityQueue[max]) {
                max = leftChild; //Set largest as leftChild
            }

            //Check if a rightChild exists and is larger than current largest index
            if (rightChild < priorityQueue.size() && priorityQueue[rightChild] > priorityQueue[max]) {
                max = rightChild; //Set largest as rightChild
            }

            //If the max variable changed
            if (max != index) {
                swap(priorityQueue[index], priorityQueue[max]); //Swap large index with current index
                downHeap(max); //Recursion of downHeap
            }
        }

        //Upheap Function | Created by Me
        void upHeap(int index) {
            int parentIndex = (index - 1) / 2; //parentIndex expression
            if (priorityQueue[index] > priorityQueue[parentIndex]) { //Check if the current is larger than parentIndex
                swap(priorityQueue[index], priorityQueue[parentIndex]); //Swap Email positions
                upHeap(parentIndex); //Recursion of upHeap
            }
        }

    public: //Unhidden Information
        PriorityQueue() {} //Constructor

        //isEmpty Function | Created by Me
        bool isEmpty() {
            return priorityQueue.empty(); //Check if vector is empty
        }

        //Size Function | Used Google Gemini
        size_t size() const {
            return priorityQueue.size(); //Return the size of the vector
        }

        //Peek Function | Used Google Gemini
        Email peek() {
            if (isEmpty() == false) { //Check if the vector is empty
                return priorityQueue.front(); //Return the highest priority Email
            } else { //Empty PriorityQueue
                throw std::runtime_error("Error 01: Empty PriorityQueue");
            }
        }

        //Remove Function | Used Google Gemini to fix 
        Email remove() {
            if (isEmpty() == false) { //Check if the vector is empty
                Email removedEmail = priorityQueue[0]; //Set the top as removedEmail
                priorityQueue[0] = priorityQueue.back(); //Change the top to the last Email in the vector
                priorityQueue.pop_back(); //Remove the last Email in the vector
                downHeap(0); //Downheap function
                return removedEmail; //Return the top
            } else { //Empty PriorityQueue
                throw std::runtime_error("Error 01: Empty PriorityQueue"); 
            }
        }

        //Add Function | Created by Me
        void add(Email email) {
            priorityQueue.push_back(email); //Add the Email to the back of the vector
            upHeap(priorityQueue.size() - 1); //upHeap the new addition
        }

};

//Priority Number Function | Created by Me
int priorityNumber(std::string sender, std::string date) {
    int priorityNum = 0;
    std::istringstream ss(date);
    if (sender == "Boss") {
        priorityNum += 500;
    } else if (sender == "Subordinate") {
        priorityNum += 300;
    } else if (sender == "Peer") {
        priorityNum += 250;
    } else if (sender == "ImportantPerson") {
        priorityNum += 100;
    }

    return priorityNum;
}

//Break Line Function | Used Google Gemini and stackOverflow
void breakLine(std::string cmdLine, PriorityQueue& pq) {
    std::istringstream iss(cmdLine);
    std::string command;
    iss >> command;

    if (command == "EMAIL") {
        std::string remaining;
        std::getline(iss >> std::ws, remaining);

        std::stringstream ss(remaining);
        std::string segment;
        std::vector<std::string> parts;
        while (std::getline(ss, segment, ',')) {
            parts.push_back(segment);
        }
        std::string sender = parts[0];
        std::string subject = parts[1];
        std::string date = parts[2];
        int priorityNum = priorityNumber(parts[0], parts[2]);
        pq.add(Email(sender, subject, date, priorityNum));

    } else if (command == "COUNT") {
        std::cout << "Number of emails in queue: " << pq.size() << std::endl;

    } else if (command == "NEXT") {
        Email nextEmail = pq.peek();
        std::cout << "Processing next email: Sender=" << nextEmail.sender
                  << ", Subject=" << nextEmail.subject << ", Date=" << nextEmail.date << std::endl;
        
    } else if (command == "READ") {
        pq.remove();
    }
}

//Main Function
int main() {
    std::cout << "Loading Assignment5_Test_File.txt..." << std::endl; //Start Program Message
    std::string cmdLine; //String Variable to store command Lines
    std::ifstream cmdFile("Assignment5_Test_File.txt"); //Access Assignment5_Test_File.txt | Used w3schools.com
    PriorityQueue pq; //Initialize a PriorityQueue
    while (std::getline (cmdFile, cmdLine)) { //Go through each line in the file
        breakLine(cmdLine, pq); //Send a line to breakLine function
    }
    cmdFile.close(); //Close the file
    std::cout << "Assignment5.cpp is Complete!" << std::endl; //End Program Message

    return 0; //Return a successful program run
}