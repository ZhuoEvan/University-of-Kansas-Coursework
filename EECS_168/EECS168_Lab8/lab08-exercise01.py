'''
Author: Evan Zhuo
KUID: 3109819
Date: 03/26/2024
Lab: lab08
Last modified: 04/01/2024
Purpose: Python-mon! Gotta Catch'em All!
'''
#Functions
def build_pokedex(filename):
    pokedex = {}
    for line in filename:
        line = line.strip()
        divided_line = line.split('\t')
        pokedex[divided_line[0]] = divided_line[1]
    return pokedex

def build_team(pokedex, size=6, is_unique=False):
    import random
    pokemon_list = []
    for pokemon in pokedex.keys():
        pokemon_list.append(pokemon)
    if is_unique == True:
        team = random.sample(pokemon_list, k=size)
    else:
        team = random.choices(pokemon_list, k=size)
    return team
    
def battle(team1, team2):
    import random
    #Team Introductions
    print('\n+++Team 1+++')
    for pokemon in team1:
        print(pokemon)
    print('\n+++Team 2+++')
    for pokemon in team2:
        print(pokemon)
    #Battle
    number = 1
    while len(team1) != 0 and len(team2) != 0:
        print(f'\n+++Round {number}+++')
        print(f'{team1[0]} VS {team2[0]}')
        number += 1
        victory = random.randint(1, 2)
        if victory == 1:
            print(f'{team2[0]} wins!')
            team1.pop(0)
        else:
            print(f'{team1[0]} wins!')
            team2.pop(0)
    if len(team1) == 0:
        print('\n+++Team 2 Wins!+++')
        for pokemon in team2:
            print(pokemon)
    else:
        print('\n+++Team 1 Wins!+++')
        for pokemon in team1:
            print(pokemon)
    
def main():
    #Pokedex
    print('Before this gigachad Evan Zhuo program begins...')
    pokedex_file = input('Please enter the pokedex file name: ')
    pokedex_data = open(pokedex_file, 'r')
    pokedex = build_pokedex(pokedex_data)
    pokedex_data.close()
    print('Starting Program\n')
    
    #Menu
    menu = 'Menu'
    menu_end = '===='
    choice = 0
    a_instruction = 0
    b_instruction = 0
    while choice != 5:
        print(menu.center(20, '='))
        print('Option 1) Print Pokedex\nOption 2) Translate')
        print('Option 3) Pokemon translation quiz\nOption 4) Pokemon battle')
        print('Option 5) Exit')
        print(menu_end.center(20, '='))
        choice = int(input('\nSelect an option by inputting a number: '))
        
        #Print Pokedex
        if choice == 1:
            title = 'Pokedex'
            print(title.center(20, '='))
            print(f'English | Japanese')
            for pokemon, j_pokemon in pokedex.items():
                print(f'{pokemon} | {j_pokemon}')
            print('====================\n')
            
        #Translate
        elif choice == 2:
            title = 'Translation'
            print(title.center(20, '='))
            if a_instruction == 0:
                print('To use this function, enter the English Pokemon name.')
                print('Make sure the first letter is capitalized, and the rest')
                print('of the name is in lowercase.\n')
                a_instruction = 1
            english_name = input('Enter a Pokemon name to translate: ')
            if english_name in pokedex.keys():
                translate = pokedex[english_name]
                print(f'Japanese name: {translate}')
            else:
                print('Pokemon is not present in Pokedex :(')
            print('====================\n')
            
        #Pokemon translation quiz
        elif choice == 3:
            import random
            failure_message = ['Better luck next time!', 'Get ready to learn Pokemon.', 'You Suck!']
            title = 'GUESS THAT POKEMON!'
            print(title.center(30, '='))
            japanese_pokemon = []
            for pokemon in pokedex.values():
                japanese_pokemon.append(pokemon)
            wild_pokemon = random.choice(japanese_pokemon)
            for pokemon in pokedex.keys():
                if pokedex[pokemon] == wild_pokemon:
                    correct_pokemon = pokemon
            if b_instruction == 0:
                print('To use this function, enter the English Pokemon name.')
                print('Make sure the first letter is capitalized, and the rest')
                print('of the name is in lowercase.')
                print('Also make sure the guess is in the pokedex!\n')
                b_instruction = 1
            print(f"Who's that Pokemon?\t[{wild_pokemon}]")
            user_guess = input('Pokemon Guess: ')
            if pokedex[user_guess] == wild_pokemon:
                print(f"It's {correct_pokemon}!")
                print(f'Correct! {user_guess} is {wild_pokemon}!')
            else:
                print(f"It's {correct_pokemon}!")
                print(random.choice(failure_message))
            print('==============================\n')
            
        #Pokemon battle
        elif choice == 4:
            title = 'POKEMON BATTLE!'
            print(title.center(30, '='))
            size = int(input('Enter a team size: '))
            if size >= 1 and size <= 6:
                unique = input('Unique teams? (y/n): ')
                if unique.lower() == 'y':
                    unique = True
                    team_one = build_team(pokedex, size, unique)
                    team_two = build_team(pokedex, size, unique)
                    battle(team_one, team_two)
                else:
                    unique = False
                    team_one = build_team(pokedex, size, unique)
                    team_two = build_team(pokedex, size, unique)
                    battle(team_one, team_two)
            else:
                print('Invalid Team Size.')
            print('==============================\n')
            
        #Invalid input
        elif choice <= 1 or choice >= 6:
            print('Invalid Input\n')
    print('Exiting Program')
main()
