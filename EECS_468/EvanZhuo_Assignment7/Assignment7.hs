{-
- Title: EECS 468 Assignment 7
- Description: Defining Haskell Functions
- Inputs: "debug" cases & "test" cases
- Output: Haskell Function Results
- Collaborators: EECS 468 Permutations & Combinations | www.tutorialspoint.com | Google Gemini
- Name: Evan Zhuo
- Date: 04/20/25
- Assignment7.hs
-}

--Part 1 - Defining Simple Haskell Functions

--replicate' function | Used Google Gemini
replicate' :: Int -> a -> [a] --Accepts an Integer and a String to produce a String in List
replicate' n x = [x | _ <- [1..n]] --A generator that runs n times will add an x into the list

--perfects function | Used www.tutorialspoint.com
perfects :: Int -> [Int] --Accepts an Integer to produce an Integer in List
--Generate values from 1 to n and checks if the current x is equal to the sum of divisors
perfects n = [x | x <- [1..n], x == sum (properDivisors x)] --Return list of numbers that are perfects
  where --Call other function (properDivisors)
    --Generate values from 1 to n-1 and checks if n modulo x is zero 
    properDivisors n = [x | x <- [1..n-1], n `mod` x == 0] --Return list with divisors

--find function | Used Google Gemini
find :: Eq a => a -> [(a,b)] -> [b] --Accepts an Integer and a List of Tuples to produce a String in List
find x pairs = [b | (a,b) <- pairs, x == a] --Go through all tuples in a list and adds b to the list if element a is equal to x

--positions function | Used Google Gemini
positions :: Eq a => a -> [a] -> [Int] --Accepts a String and a List of Strings to produce an Integer in List
positions x xs = find x (zip xs [0..]) --Create tuples with String List and numbers starting at 0. Call find with x and new tuples and return list result

--scalarproduct function | Used Google Gemini
scalarproduct :: [Int] -> [Int] -> Int --Accepts two List of Integers to produce an Integer
scalarproduct xs ys = sum[a * b | (a,b) <- zip xs ys] --Create tuples from the two lists and then sum the products of every tuple

--Part 2 - Defining Haskell Functions for Distributing Objects into Boxes

--Distinguishable Objects into Distinguishable Boxes | Used Google Gemini
dodb n k m = fac n / (denominator n k m) --Permutations with Indistinguishable Objects Formula
  where
    --Denominator Equation: m! for k times multiplied by total (n) minus m * k (mimics (52-20)!)
    denominator n k m = product [fac m | _ <- [1..k]] * (fac (n - (m * k))) 
    fac 0 = 1 --Factorial Function for 0
    fac n = product [1..n] --Factorial Function for n > 1 | Used Google Gemini Here

--Indistinguishable Objects into Distinguishable Boxes | Created by Me
iodb n k = numerator n k / denominator n k --Combinations with Repetition Formula
  where
    numerator n k = fac (n+k-1) --Numerator of the Combinations with Repetition Formula ((n + k - 1)!)
    denominator n k = fac n * fac(k-1) --Denominator of the Combinations with Repetition Formula (n!(k-1)!)
    fac 0 = 1 --Factorial Function for 0
    fac n = product [1..n] --Factorial Function for n > 1

--Distinguishable Objects into Indistinguishable Boxes
doib n k = sum[combination n j | j <- [1..k]] --Sum of combinations
  where
    combination n k = fac n / (fac k * fac (n-k)) --Combination Formula
    fac 0 = 1 --Factorial Function for 0
    fac n = product [1..n] --Factorial Function for n > 1

--Indistinguishable Objects into Indistinguishable Boxes | Used Google Gemini
ioib n k = p (n - k) k + p n (k - 1) --Start first recursive call
  where
    p n k --Cases for p function
      | k < 1 || n < 0 = 0 --Return 0 if k is less than 1 or n is less than 1
      | k == 1 = 1 --Return 1 if k is equal to 1
      | n == 0 = 1 --Return 1 if n is equal to 0
      | otherwise = p (n - k) k + p n (k - 1) --Recursive call on the recursive algorithm from EECS 468 Permutations & Combinations

{- Test Case -}