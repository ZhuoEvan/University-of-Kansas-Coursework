{-
- Title: EECS 468 Assignment 9
- Description: Game of Nim in Haskell
- Inputs: User Inputs
- Output: Game of Nim Board
- Collaborators: Google Gemini
- Name: Evan Zhuo
- Date: 05/06/25
- Assignment9.hs
-}

import System.IO --Import System.IO Library
import Data.Char (isDigit) --Import isDigit Function from Data.Char Library
import Data.Char (digitToInt) --Import digitToInt Function from Data.Char Library

type Board = [Int] --Declare a Board Type (A list of integers) | Used Assignment 9 Instructions

initial :: Board --Declare initial as a Board Type | Used Assignment 9 Instructions
initial = [5,4,3,2,1] --Assign the list of integers to initial

clear :: Board -> Bool --Clear Function with Board type to Boolean | Created by Me, Used Google Gemini to fix syntax error
clear [] = True --Empty List returns true
clear (x:xs) = x == 0 && clear xs --Check first element in list then recurse to the next element until all elements have been checked

swapTurn :: Int -> Int --Swap Turn Function with Integer to Integer Type | Created by Google Gemini
swapTurn 1 = 2 --Change 1 to 2
swapTurn 2 = 1 --Change 2 to 1

victory :: Int -> IO () --Victory Function with Integer to IO () | Created by Me, Used Google Gemini for '$'
victory player = do --Writes the player number into the string
    putStrLn $ "Player " ++ show player ++ " wins!" --Prints the Winning Player and ends the program

display :: Board -> IO () --Display Board Function with Board | Used Google Gemini
display board = sequence_ (map displayRow (zip [1..] board)) --Correlate row number with star number

displayRow :: (Int, Int) -> IO () --Display Row Function with Tuple of two Integers to IO () | Used Google Gemini
displayRow (rowNum, numStars) = do --Take the tuple from zip and assign rowNum and numStars
    putStr (show rowNum ++ ": ") --Print row number and ':'
    putStrLn (replicate numStars '*')  --Print the number of stars

getInput :: String -> IO Int --Scan Input Function with String to IO Integer | Used Google Gemini
getInput prompt = do --Assign the String (input message) to prompt
    putStrLn prompt --Print the input message
    input <- getLine --Get string from user and assign it to input
    if all isDigit input && not (null input) --Check if input is a digit and not empty
       then return (read input) --Return the integer
       else do
            putStrLn "ERROR: Not a number" --Error Message for writing anything other than an integer
            getInput prompt --Repeat the process for valid input

playerMove :: Board -> Int -> IO Board --Player Move Function with Board and Integer to IO Board | Used Google Gemini
playerMove board player = do --Assign Board to board and Integer to player 
    putStrLn ("Player " ++ show player) --Print player then player number
    row <- getInput "Enter a row number: " --Print input message then get an input for row
    removeStar <- getInput "Stars to remove: " --Print input message then get an input for removeStar
    let rowIndex = row - 1 --Create a variable rowIndex and assign it row - 1
    if rowIndex < 0 || rowIndex >= length board || removeStar <= 0 then do --Check if row is on the board or removeStar is positive
      putStrLn "ERROR: Invalid move" --Error Message for Invalid input
      playerMove board player --Repeat the process for valid input
    else do --Another invalidation check
      let currentRowValue = board !! rowIndex --Get number of stars from the board using row information
      if removeStar > currentRowValue then do --Check if removeStar is possible
        putStrLn "ERROR: Invalid move" --Error Message for Invalid input
        playerMove board player --Repeat the process for valid input
      else --No invalid conditions
        let newBoard = zipWith (\i v -> if i == rowIndex then v - removeStar else v) [0..] board --Update the board with stars removed
        in return newBoard --Return updated board

play :: Board -> Int -> IO () --Play Function with Board and Integer Type to IO () | Used Assignment 9 Instructions & Google Gemini
play board player = do --Take board and player number
    putChar '\n' --Print an empty line above the board
    display board --Print the current board
    putChar '\n' --Print an empty line below the board
    newBoard <- playerMove board player --Create a new board after the move function
    if clear newBoard --Check if the board is empty
       then victory player --Finish the game
       else play newBoard (swapTurn player) --Repeat play but with the players swapped

nim :: IO () --Nim Function with IO Type | Used Assignment 9 Instructions
nim = play initial 1 --Start game of nim

main :: IO () --Main Function | Created by Me
main = nim --Start the game of nim