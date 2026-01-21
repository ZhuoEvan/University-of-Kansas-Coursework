#miniProject1.1.py

#Task 1 Vigenere Cipher

#Python Library
import datetime

#Global Variables
alphabetDict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3,
    'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'J': 9, 'K': 10, 'L': 11,
    'M': 12, 'N': 13, 'O': 14, 'P': 15,
    'Q': 16, 'R': 17, 'S': 18, 'T': 19,
    'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25
}

bar = '=============================='

#Encryption Function
def encryption(m, K):
    m = letterToNum(m)
    K = letterToNum(K)
    result = (m + K) % 26
    result = numToLetter(result)
    return result

#Decryption Function
def decryption(m, K):
    m = letterToNum(m)
    K = letterToNum(K)
    result = (m - K) % 26
    result = numToLetter(result)
    return result

#Letter Convertor Function
def letterToNum(letter):
    num = alphabetDict.get(letter)
    return num
    
#Number Convertor Function
def numToLetter(num):
    letter = retrieveKey(num)
    return letter

#Dictionary Key Retrieve Function
def retrieveKey(searchValue):
    for key, value in alphabetDict.items():
        if searchValue == value:
            return key
    #Error Check: Key Does Not Exist
    raise RuntimeError("Error 01: Key Does Not Exist Error.")

#Apply Key Function
def applyKey(message, key):
    #Local Variables
    keyLength = len(key)
    encryptChar = []

    stringList = splitMessage(message, keyLength)
    for string in stringList:
        keyIndex = 0
        for char in string:
            encryptChar.append(encryption(char, key[keyIndex]))
            keyIndex += 1

    encryptedMessage = ''.join(encryptChar)
    return encryptedMessage

#Remove Key Function
def removeKey(message, key):
    #Local Variables
    keyLength = len(key)
    decryptChar = []
    
    stringList = splitMessage(message, keyLength)
    for string in stringList:
        keyIndex = 0
        for char in string:
            decryptChar.append(decryption(char, key[keyIndex]))
            keyIndex += 1
    
    decryptedMessage = ''.join(decryptChar)
    return decryptedMessage

#Message Split Function
def splitMessage(message, keyLength):
    #Local Variables
    splitMessage = []
    combinedChar = ''
    currentIndex = 1

    #Split the Message into keyLength Size
    for char in message:
        combinedChar = combinedChar + char
        if currentIndex % keyLength == 0:
            splitMessage.append(combinedChar)
            combinedChar = '' #Reset combinedChar
        currentIndex += 1 #Increment the currentIndex
    
    #Append Remaining Characters
    if len(combinedChar) != 0:
        splitMessage.append(combinedChar)
    
    return splitMessage #Return List

#Menu Function
def menu():
    print(f'{bar}\nVigenere Cipher\n1) Encryption\n2) Decryption\n3) Quit\n{bar}')
    return

#New Line Function
def newLine():
    print('')
    return

#Main Function
def main():
    #Local Variables
    choice = 0

    while choice != 3:
        menu()
        choice = int(input("Enter 1/2/3-> "))
        newLine()
        if choice == 1:
            user_msg = str(input('(1/2) Enter Message: '))
            user_key = str(input('(2/2) Enter Key: '))
            print(applyKey(user_msg.upper(), user_key.upper()))
            newLine()

        elif choice == 2:
            user_c_msg = str(input('(1/2) Enter Message: '))
            user_key = str(input('(2/2) Enter Key: '))
            print(removeKey(user_c_msg.upper(), user_key.upper()))
            newLine()

        elif choice == 3:
            newLine()

        else:
            print("~~~Error 01: Invalid Option~~~")
    
    print("~~~ Terminating Program... ~~~")

main()