'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/11/2024
Lab: lab01
Last modified: 9/15/2024
Purpose: User Input and File Opening Board Game
'''
#executive.py

#Importing Class
from boardgame import BoardGame

#Global Variables
bar = '===================='

#Creation of the Executive Class
class Executive:
    
    #Initial Values
    def __init__(self, file_name):
        self.file_name = file_name
        
    #The program will start from run
    def run(self):
        valid_bg = []
        board_games_storage = []
        board_games_list = self.open_file()
        #Error Check: All Data Filled Out
        for item in board_games_list:
            try:
                if len(item) != 6:
                    raise ValueError('Missing Component')
                else:
                    valid_bg.append(item)
            except:
                error_missing = f'This board game: '
                error_missing += f'{item} has missing component(s)'
                print(error_missing)
        #Assigning the infomation
        for bg in valid_bg:
            board_game = BoardGame(bg[0], float(bg[1]), float(bg[2]), float(bg[3]), bg[4], bg[5])
            board_games_storage.append(board_game)
        #Begin Accepting User's Command
        self.user_action(board_games_storage)

    #This function takes user's commands
    def user_action(self, storage):
        self.storage = storage       
        #User Menu Selection
        choice = '0'
        while choice != '6':
            print(f'{bar}{bar}{bar}\n{self.menu()}\n{bar}{bar}{bar}')
            choice = input('Enter Choice: ')
            #Print All Games Highest Gibbons Rating to Lowest
            if choice == '1':
                self.rating_sort(self.storage)
            #Print All Games From a Year
            elif choice == '2':
                self.year_search(self.storage)
            #Print All Games With a Weight Equal to or Lower Than a Provided Weight
            elif choice == '3':
                self.weight_check(self.storage)
            #The People VS Dr. Gibbons
            elif choice == '4':
                self.rating_compare(self.storage)
            #Print Based on Player Count
            elif choice == '5':
                self.player_count(self.storage)
            #Exit the Program
            elif choice == '6':
                pass
            else:
                print('Invalid Input')               
        #Prompt to Exit
        input('Press Enter Key to Exit the Program')

    #Extracting the User File  
    def open_file(self):
        clean_bg_list = []
        board_games_list = []
        with open(self.file_name, errors='ignore') as user_file:
            #Cleaning up the elements
            for element in user_file:
                new_element = element.strip()
                clean_bg_list.append(new_element)
            for line in clean_bg_list:
                data = line.split('\t')
                board_games_list.append(data)
            #Removing the title line
            board_games_list.pop(0)
        return board_games_list

#User Action Functions
    
    #Sorting the Rating from Highest to Lowest with sorted() function
    def rating_sort(self, storage):
        self.storage = storage
        sorted_list = sorted(self.storage, reverse=True)
        for board_game in sorted_list:
            print(board_game)

    #Checking the Board Game List and Selecting Only the Same Year Board Games
    def year_search(self, storage):
        self.storage = storage
        #Error Check: Valid Year Input
        try:
            bg_year_list = []
            user_year = int(input('Enter a Year: '))
            user_year_str = str(user_year)
            for board_game in self.storage:
                if board_game._year == user_year_str:
                    bg_year_list.append(board_game)
        except:
            print(self.questionmark())
        if len(bg_year_list) == 0:
            print('No Games Exist')
        else:
            for board_game in bg_year_list:
                print(board_game)
    
    #Checking the Board Game List and Comparing with User Inputted Weight
    def weight_check(self, storage):
        self.storage = storage
        #Error Check: Valid Weight Number
        try:
            weight_list = []
            user_weight = float(input('Enter a Weight: '))
            if user_weight < 0 or user_weight > 5:
                raise ValueError('Invalid Weight Number')
            else:
                for board_game in self.storage:
                    if board_game._avgweight <= user_weight:
                        weight_list.append(board_game)
        except:
            print(self.questionmark())
        if len(weight_list) == 0:
            print('No Games Exist')
        else:
            for board_game in weight_list:
                print(board_game)
                
    #Subtracting Both Ratings for All Board Games Then Doing An Inequality
    def rating_compare(self, storage):
        self.storage = storage
        #Error Check: Valid Rating Number
        try:
            rating_check = []
            user_rating = float(input('Enter a Rating Number: '))
            if user_rating < 0 or user_rating > 10:
                raise ValueError('Invalid Rating Number')
            else:
                for board_game in self.storage:
                    compare_value0 = board_game._rating - board_game._baverage
                    compare_value1 = abs(compare_value0)
                    if compare_value1 <= user_rating:
                        rating_check.append(board_game)
        except:
            print(self.questionmark())
        if len(rating_check) == 0:
            print('No Games Exist')
        else:
            for board_game in rating_check:
                print(board_game)
                
    #Checking the bbgbestplayers number with User Number
    def player_count(self, storage):
        self.storage = storage
        #Error Check: Valid Player Count Number
        try:
            bbgbestplayers_list = []
            user_player_count = int(input('Enter a Player Count: '))
            if user_player_count <= 0:
                raise ValueError('Negative Friends? That is rough')
            else:
                for board_game in self.storage:
                    index = board_game._bbgbestplayers.split(',')
                    for i in index:
                        if int(i) == user_player_count:
                            bbgbestplayers_list.append(board_game)
        except:
            print(self.questionmark())
        if len(bbgbestplayers_list) == 0:
            print('No Games Exist')
        else:
            for board_game in bbgbestplayers_list:
                    print(board_game)
            
#Large Text Functions

    #Creating the user interface
    def menu(self):
        menu = '1)Print all games highest Gibbons rating to lowest\n'
        menu += '2)Print all games from a year\n'
        menu += '3)Print all games with a weight equal to or lower than '
        menu += 'a provided weight\n'
        menu += '4)The People VS Dr. Gibbons\n'
        menu += '5)Print based on player count\n'
        menu += '6)Exit the program'
        return menu
    
    #A massive question mark (I think it's funny)
    def questionmark(self):
        qm = f'  ?????????\n'
        qm += f'?????????????\n'
        qm += f'?????????????\n'
        qm += f'????     ????\n'
        qm += f'????     ????\n'
        qm += f'       ????\n'
        qm += f'       ????\n'
        qm += f'     ????\n'
        qm += f'     ????\n'
        qm += f'\n'
        qm += f'     ????\n'
        qm += f'     ????\n'
        return qm



