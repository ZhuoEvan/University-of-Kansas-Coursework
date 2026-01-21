#finalproject.py

#PushDownAutomata Class
class PushDownAutomata:
    #PushDownAutomata Class Constructor
    def __init__ (self, states, alphabet, stackAlphabet, startState, endState, transitions):
        self._states = states
        self._alphabet = alphabet
        self._stackAlphabet = stackAlphabet
        self._startState = startState
        self._endState = endState
        self._transitions = transitions
        self.stack = ['/']
        self.path = []
    
    #Stack Push Helper Function
    def push(self, entry):
        self.stack.append(entry)
    
    #Stack Pop Helper Function
    def pop(self):
        self.stack.pop(-1)
    
    #Stack Manipulation Function
    def stackAppend(self, entry_list):
        self.pop()
        for entry in reversed(entry_list):
            self.push(entry)
    
    #Path Trace Function
    def pathTrace(self, currState, symbol, newState, currStack):
        currPath = []
        currPath.append(currState)
        currPath.append(symbol)
        currPath.append(newState)
        currPath.append(currStack)
        self.path.append(currPath)

    #Transition Reader Function
    def readTransition(self, ptr, currState, symbol, stackElem):
        #Local Variables
        space = ' '
        specialChar = ['(', ')', '{', '}', ';']
        currStack = []
        for stackVar in self.stack:
            currStack.append(stackVar)

        #Transitions
        for transition in self._transitions:
            t = transition #use transition as t

            #Deciphering Special Characters
            if symbol != space and stackElem != 'C' and symbol in specialChar:
                if currState == t[0] and symbol in t[5] and stackElem == t[3]:
                    newState = t[2]
                    self.stackAppend(t[5])
                    break

                elif currState == t[0] and symbol == stackElem and stackElem == t[3]:
                    newState = t[2]
                    self.stackAppend(t[5])
                    ptr += 1
                
            #Deciphering Characters
            elif symbol != space:
                if currState == t[0] and symbol == t[5] and stackElem == t[3]:
                    newState = t[2]
                    self.stackAppend(t[5])
                    break

                elif currState == t[0] and symbol == stackElem and stackElem == t[3]:
                    newState = t[2]
                    self.stackAppend(t[5])
                    ptr += 1
                    break
                
                elif currState == t[0] and stackElem == t[3] and "C" in t[5]:
                    newState = t[2]
                    self.stackAppend(t[5])
                    break

                elif currState == t[0] and stackElem == t[3]:
                    newState = t[2]
                    self.stackAppend(t[5])

            #Deciphering Space
            elif symbol == space:
                if currState == t[0] and stackElem == '_' and stackElem == t[3]:
                    newState = t[2]
                    self.stackAppend(t[5])
                    ptr += 1
                    break

                elif currState == t[0] and stackElem == 'U' and stackElem == t[3]:
                    newState = t[2]
                    self.stackAppend(t[5])
                    break
                
                elif currState == t[0] and stackElem == t[3] and "U" in t[5]:
                    newState = t[2]
                    self.stackAppend(t[5])
                    break
        
        self.pathTrace(currState, symbol, newState, currStack)
        #return pointer and newState
        return ptr, newState
    

    #First Run Function
    def firstRun(self, w):
        #Initial Variables
        ptr = 0
        currentState = self._startState
        currentSymbol = w[ptr]
        currentStackElem = self.stack[-1]

        ptr, newState = self.readTransition(ptr, currentState, currentSymbol, currentStackElem)
        return newState

    #Run Function
    def run(self, w):
        currentState = self.firstRun(w)
        ptr = 0

        while ptr != len(w):
            currentSymbol = w[ptr]
            currentStackElem = self.stack[-1]
            #Remove "lambda" from Stack
            if currentStackElem == '/':
                self.pop()
                currentStackElem = self.stack[-1]
            
            ptr, currentState = self.readTransition(ptr, currentState, currentSymbol, currentStackElem)
        
        #Accept
        if currentState == self._endState and self.stack[0] == '/':
            print("Accept")
            self.pathTrace(currentState, '/', self._endState, self.stack) #Append final path
            #Print out the paths
            for p in self.path:
                print(f'{p[0]} {p[1]} {p[2]} | Stack: {p[3]}')
            return True
        #Reject
        else:
            print("Reject")
            return False
    
#Accept Function
def accept(A, w):
    A.run(w)

#Load File Function
def load(loadFile):
    #Local Variables
    loadValues = []
    transitionValues = []
    currentLineCount = 0
    isTransition = False
    
    #Access File Data
    with open(loadFile) as openFile: #Open the file
        for line in openFile: #Access each line of data in the file
            if currentLineCount > 4: 
                isTransition = True
            
            if isTransition:
                transitionValues.append(line.strip().split())
            else:
                loadValues.append(line.strip().split())
            currentLineCount += 1
    
    loadValues.append(transitionValues) #Finalize the loadValues
    return loadValues

#Main Function
def main():
    loadValues = load("load.txt")
    lv = loadValues #Use loadValues as lv
    myPDA = PushDownAutomata(lv[0], lv[1], lv[2], lv[3][0], lv[4][0], lv[5])
    myString = input("Enter a string: ")
    #myString = "void func(param) {funcdef;}" test string
    accept(myPDA, myString)

main()