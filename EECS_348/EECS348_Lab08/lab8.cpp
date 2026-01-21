#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <sstream>

using namespace std; //Reduce the width of the code by removing std::

//Print Function
void print(const vector<vector<int>>& matrix, const int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (matrix[i][j] < 10) {
                cout << "0" << matrix[i][j] << " ";
            } else {
                cout << matrix[i][j] << " ";
            }
        }
        cout << endl;
    }
    cout << endl;
}

//Out of Bounds Function
void oob() {
    cout << "Error 01: Out of Bounds" << endl;
}

//Bound Check Function
bool bound(int user, const int n) {
    if (user > n) {
        oob();
        return false;
    } else {
        return true;
    }
}

//Swap Row Function
void swapRow(const int row1, const int row2, const vector<vector<int>>& matrix, const int n) {
    vector<vector<int>> tempMatrix = matrix;
    if (bound(row1, n) && bound(row2, n)) {
        for (int i = 0; i < n; ++i) {
            tempMatrix[row1][i] = matrix[row2][i];
            tempMatrix[row2][i] = matrix[row1][i];
        }
        cout << "Swap Row Matrix Display" << endl;
        print(tempMatrix, n);
    }
}

//Swap Column Function
void swapCol(const int col1, const int col2, const vector<vector<int>>& matrix, const int n) {
    vector<vector<int>> tempMatrix = matrix;
    if (bound(col1, n) && bound(col2, n)) {
        for (int i = 0; i < n; ++i) {
            tempMatrix[i][col1] = matrix[i][col2];
            tempMatrix[i][col2] = matrix[i][col1];
        }
        cout << "Swap Row Matrix Display" << endl;
        print(tempMatrix, n);
    }
}

//Replace Function
void replace(const int row, const int col, const vector<vector<int>>& matrix, const int value, const int n) {
    vector<vector<int>> tempMatrix = matrix;
    if (bound(row, n) && bound(col, n)) {
        tempMatrix[row][col] = value;
        cout << "Replacement Matrix Display" << endl;
        print(tempMatrix, n);
    }
}

//Add Function
void add(const vector<vector<int>>& matrix1, const vector<vector<int>>& matrix2, const int n) {
    vector<vector<int>> resultMatrix(n, vector<int>(n));
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            resultMatrix[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }
    cout << "Add Matrix Display" << endl;
    print(resultMatrix, n);
}

//Multiply Function
void multiply(const vector<vector<int>>& matrix1, const vector<vector<int>>& matrix2, const int n) {
    vector<vector<int>> resultMatrix(n, vector<int>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int sum = 0;
            for (int k = 0; k < n; ++k) {
                int product = matrix1[i][k] * matrix2[k][j];
                sum += product;
            }
            resultMatrix[i][j] = sum;
        }
    }

    cout << "Multiply Matrix Display" << endl;
    print(resultMatrix, n);
}

//Diagonal Function
void diagonal(vector<vector<int>>& matrix, const int n) {
    int mainSum = 0;
    int secSum = 0;
    
    for (int i = 0; i < n; i++) {
        mainSum += matrix[i][i];
        secSum += matrix[i][(n-1) - i];
    }
    
    cout << "Main Diagonal Elements Sum: " << mainSum << endl;
    cout << "Secondary Diagonal Elements Sum: " << secSum << endl;
}

//Main Function
int main() {
    cout << "[Starting lab8.cpp Program]" << endl; //Start Program Message
    //string fileName; //string to hold file name
    string fileName = "matrix.txt";
    int n; //integer to hold matrix size
    vector<vector<int>> matrix1;
    vector<vector<int>> matrix2;

    cout << "Enter file name with dot extension!" << endl;
    //cin >> fileName;
    
    //Extracting the data from the file
    ifstream inputFile(fileName);
    inputFile >> n;
    matrix1.resize(n, vector<int>(n)); //Resize Function used Google Gemini
    matrix2.resize(n, vector<int>(n)); //Resize Function used Google Gemini
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            inputFile >> matrix1[i][j];
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            inputFile >> matrix2[i][j];
        }
    }
    inputFile.close();
    
    //Print Matrices
    cout << "Matrix 1" << endl;
    print(matrix1, n);
    cout << "Matrix 2" << endl;
    print(matrix2, n);
    
    //Add and Multiply
    add(matrix1, matrix2, n);
    multiply(matrix1, matrix2, n);
    
    //Diagonal Sums
    cout << "Matrix 1" << endl;
    diagonal(matrix1, n); cout << endl;
    cout << "Matrix 2" << endl;
    diagonal(matrix2, n);
    
    //Swapping Rows
    int row1, row2;
    cout << "Enter a row to swap (1/2): ";
    cin >> row1;
    cout << "Enter a row to swap (2/2): ";
    cin >> row2;
    cout << "Matrix 1" << endl;
    swapRow(row1, row2, matrix1, n);
    cout << "Matrix 2" << endl;
    swapRow(row1, row2, matrix2, n);
    
    //Swapping Columns
    int col1, col2;
    cout << "Enter a column to swap (1/2): ";
    cin >> col1;
    cout << "Enter a column to swap (2/2): ";
    cin >> col2;
    cout << "Matrix 1" << endl;
    swapCol(col1, col2, matrix1, n);
    cout << "Matrix 2" << endl;
    swapCol(col1, col2, matrix2, n);
    
    //Replacement
    int newRow, newCol, newVal;
    cout << "Enter a row to swap (1/3): ";
    cin >> newRow;
    cout << "Enter a column to swap (2/3): ";
    cin >> newCol;
    cout << "Enter value to replace (3/3): ";
    cin >> newVal;
    cout << "Matrix 1" << endl;
    replace(newRow, newCol, matrix1, newVal, n);
    cout << "Matrix 2" << endl;
    replace(newRow, newCol, matrix2, newVal, n);
    
    cout << "[lab8.cpp program is complete!]" << endl; //Completion Message
    return 0; //Show successful run of program
    
}