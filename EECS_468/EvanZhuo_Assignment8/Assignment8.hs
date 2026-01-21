{-
- Title: EECS 468 Assignment 8
- Description: Versatile Arithmetic Expression Evaluator
- Inputs: Valid or Invalid Expressions
- Output: Solution or Error Message
- Collaborators: EECS 468 Lecture Slides (Haskell Parsing Example) | Google Gemini | Deepseek
- Name: Evan Zhuo
- Date: 04/27/25
- Assignment8.hs
-}

--Parsing Expression Function | Used Google Gemini
parse :: String -> Int --Type Conversion (String to Int)
parse expr = rpn (shunt (parseTokens expr)) --Main Function from EECS 468 Lecture Slides

--Display Operation Function | Used EECS 468 Lecture Slides
data Op = Add | Sub | Mul | Div | Mod | Exp --Types of Operation
    deriving (Eq) --Allows Equal == Function | Used Google Gemini
instance Show Op where
    show Add = "+" --Display + for Addition
    show Sub = "-" --Display - for Subtraction
    show Mul = "*" --Display * for Multiplication
    show Div = "/" --Display / for Division
    show Mod = "%" --Display % for Modulo
    show Exp = "**" --Display ** for Exponent

--Display Token Function | Used EECS 468 Lecture Slides
data Token = Num Int | Op Op | LeftParen | RightParen --Types of Token
    deriving (Eq) --Allows Equal == Function | Used Google Gemini
instance Show Token where
    show (Num n) = show n --Display Digit 0-9
    show (Op o) = show o --Display Operation +-*/
    show LeftParen = "(" --Display Left Parentheses
    show RightParen = ")" --Display Right Parentheses

--Precedence (PEMDAS) Function | Used Google Gemini
precedence :: Op -> Int --Type Conversion (Operation to Integer)
precedence Add = 1 --Assign Addition to 1 - Last Priority
precedence Sub = 1 --Assign Subtraction to 1 - Last Priority
precedence Mul = 2 --Assign Multiplication to 2
precedence Div = 2 --Assign Division to 2
precedence Mod = 2 --Assign Modulo to 2
precedence Exp = 3 --Assign Exponent to 3 - First Priority

--Digit Function (Helper) | Used Google Gemini
isDigit :: Char -> Bool --Type Conversion (Character to Boolean)
isDigit c = c >= '0' && c <= '9' --Checks if the character is a digit 0-9

--Operator Function (Helper) | Used Google Gemini
isOperator :: Char -> Bool --Type Conversion (Character to Boolean)
isOperator c = c `elem` "+-*/%^" --Check if the character is one of the operators +-*/

--Parse Number Function | Used Google Gemini
parseNumber :: String -> (Int, String) --Type Conversion (String to a Tuple of Integer and String)
parseNumber str =
    let (numStr, rest) = span isDigit str --Split digits from operators
    in  case reads numStr :: [(Int, String)] of --Access Tuple List of Integers and Strings
        [(num, "")] -> (num, rest) --No Problems Encountered with Parsing
        _           -> error "[Error 08: Invalid Number]" --Raise Error

--Parse Tokens Function | Used Deepseek
parseTokens :: String -> [Token] --Type Conversion (String to a List of Tokens)
parseTokens "" = [] --Return Empty String after encountering an Empty List
parseTokens ('-' : cs) = --Subtraction or Negative token
    case cs of
        [] -> [Op Sub]  --Check for subtraction operation
        c:cs' | isDigit c -> --Next token is a digit
            let (num, rest) = parseNumber (c:cs') --Assign negative sign to digit
            in Num (-num) : parseTokens rest --Convert to negative number
        '(':_ -> Op Sub : parseTokens cs  --Subtraction token (parenthesis case)
        _ -> Op Sub : parseTokens cs --Subtraction token
parseTokens (c : cs) --Check token in the list of tokens
    | c == '+' = Op Add : parseTokens cs --Addition token
    | c == '*' = --Exponent or Multiplication token
        case cs of
            '*' : rest -> Op Exp : parseTokens rest --Exponent token
            _ -> Op Mul : parseTokens cs --Multiplication token
    | c == '/' = Op Div : parseTokens cs --Division token
    | c == '%' = Op Mod : parseTokens cs --Modulo token
    | c == '(' = LeftParen : parseTokens cs --Left parenthesis token
    | c == ')' = RightParen : parseTokens cs --Right parenthesis token
    | isDigit c =
        let (num, rest) = parseNumber (c : cs) --Parsing the number
        in Num num : parseTokens rest --Getting the number
    | c == ' ' = parseTokens cs --Ignore spaces
    | otherwise = error ("[Error 05: Invalid Characters]") --Raise Error

--Shunt Function | Used Deepseek
shunt :: [Token] -> [Token] --Type Conversion (List of Tokens to a List of Tokens)
shunt tokens = shunt' tokens [] [] --Two empty lists
  where
    shunt' :: [Token] -> [Token] -> [Token] -> [Token] --Type Conversion (List of Tokens, List of Tokens, and List of Tokens to a List of Tokens)
    shunt' [] stack output --Output Stack
        | LeftParen `elem` stack = error "[Error 01: Unmatched Parentheses]" --Raise Error
        | otherwise = output ++ reverse stack --Access the top of the Stack
    shunt' (t:ts) stack output = case t of --Check current token
        Num n -> shunt' ts stack (output ++ [Num n]) --Detected a number - Go to the next token
        Op op -> let (opsToPush, newStack) = popHigherPrecedence op stack --Detected an operator
                 in shunt' ts (Op op : newStack) (output ++ opsToPush) --Recursive call to do the operation
        LeftParen -> shunt' ts (LeftParen : stack) output --Left parenthesis detected
        RightParen -> case popUntilParen stack of --Right parenthesis detected
            (Just (popped, newStack)) -> shunt' ts newStack (output ++ popped) --Do the operations in the new stack for parenthesis
            Nothing -> error "[Error 01: Unmatched Parentheses]" --Raise Error
    --Pop Higher Precedence Function | Used Deepseek
    popHigherPrecedence :: Op -> [Token] -> ([Token], [Token]) --Type Conversion (Operation, List of Tokens to a Tuple of a List of Tokens and a List of Tokens)
    popHigherPrecedence op [] = ([], []) --Return an Empty Stack if both stacks are empty
    popHigherPrecedence op (LeftParen:rest) = ([], LeftParen:rest) --Return Left Parenthesis
    popHigherPrecedence op1 (Op op2:rest) --Encountering another operator
        | precedence op2 >= precedence op1 = --Compare precendence of operators
            let (moreOps, newRest) = popHigherPrecedence op1 rest --Recurse
            in (Op op2 : moreOps, newRest) --New Tuple
        | otherwise = ([], Op op2:rest) --Lower Precedence
    popHigherPrecedence _ (t:rest) = error "[Error 02: Operators Without Operands]" --Raise Error
    --Pop Until Parenthesis | Used Deepseek
    popUntilParen :: [Token] -> Maybe ([Token], [Token]) --Type Conversion (List of Token to a Maybe of a Tuple of Two List of Tokens)
    popUntilParen [] = Nothing --Empty Stack means Pop is Completed
    popUntilParen (LeftParen:rest) = Just ([], rest) --Remove the left parenthesis
    popUntilParen (t:rest) = case popUntilParen rest of --Pop Cases
        Just (popped, newRest) -> Just (t:popped, newRest) --Pop and Repeat
        Nothing -> Nothing --Pop is Completed

--Apply Operation Function | Used Google Gemini
apply :: Op -> Int -> Int -> Int --Type Conversion (Operator, Integer, Integer to Integer)
apply Add x y = x + y --Add x and y
apply Sub x y = x - y --Subtract x and y
apply Mul x y = x * y --Multiply x and y
apply Div x 0 = error "[Error 03: Division by Zero is Invalid]" --Raise Error
apply Div x y = x `div` y --Divide x and y
apply Mod x 0 = error "[Error 03: Division by Zero is Invalid]" --Raise Error
apply Mod x y = x `mod` y --Modulo x and y
apply Exp x y = x ^ y --Exponent x and y

--Reverse Polish Notation Evaluation Function | Used Deepseek
rpn :: [Token] -> Int --Type Conversion (List of Tokens to an Integer)
rpn tokens = case rpnEval [] tokens of
    [result] -> result --Return final Number as Result
    _ -> error "[Error 07: Invalid RPN Expression]" --Raise Error
  where
    --Evaluate RPN Function | Used Deepseek
    rpnEval :: [Int] -> [Token] -> [Int] --Type Conversion (List of Integers and List of Tokens to a List of Integers)
    rpnEval stack [] = stack --Empty List is a Stack
    rpnEval stack (Num n : rest) = rpnEval (n : stack) rest --Pushing onto the Stack
    rpnEval (x:y:stack) (Op op : rest) = rpnEval (apply op y x : stack) rest --Evaluation of the stacks
    rpnEval _ _ = error "[Error 07: Invalid RPN Expression]" --Raise Error