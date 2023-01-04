import string
import constants

ABC = string.ascii_letters
ABC = list(ABC)
ABC.remove('a')
ABC.remove('b')
ABC.remove('A')
ABC.remove('B')
ABC_2 = ABC
ABC_2.remove('C')
ABC_2.remove('c')

PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS

def clean_constant(data):
    new_players = [] #creating new list to hold cleaned data
    for player in data: #start loop through list of player dictionaries
        every_player = {}# creating new dictionary
        every_player['name'] = player['name']#Keeping player names the same
        every_player['guardians'] = player['guardians'] #Keeping guardians the same
        if player['experience'] == 'YES': #Changing experiance to boolean
            every_player['experience'] = True
        else:
            every_player['experience'] = False
        heights = player['height']#pulling out strings
        heights= heights.replace('inches','')# taking out "inches"
        heights=int(heights)#converting str in int
        every_player['height']= heights #adding heights to new dictionary
        new_players.append(every_player) #appending dictionaries to list
    return new_players #returning our list

#Storing cleaned list in variable.
clean_players = (clean_constant(PLAYERS))

#slicing lists to create balance teams
def pick_team_1(list):
    team_1 = []
    team_1 = list[0:6]
    return (team_1)


def pick_team_2(list):
    team_2 = []
    team_2 = list[6:12]
    return (team_2)


def pick_team_3(list):
    team_3 = []
    team_3 = list[12:18]
    return (team_3)


#storing balanced team by team name
team_1 = pick_team_1(clean_players)

team_2 = pick_team_2(clean_players)

team_3 = pick_team_3(clean_players)

#Function that is supposed to extract names from list of dictionaries and store them to be displayed
def extract_names(*args):
    team_1_names = []
    team_2_names = []
    team_3_names = []
    
    for dictionary in team_1:
        if type(dictionary) == dict:
            team_1_names.append(dictionary['name'])
            
    for dictionary in team_2:
        if type(dictionary) == dict:
            team_2_names.append(dictionary['name'])
            
    for dictionary in team_3:
        if type(dictionary) == dict:
            team_3_names.append(dictionary['name'])
            
    return team_1_names, team_2_names, team_3_names



#Storing names of players in   
team_1_names = (extract_names(team_1, team_2, team_3)[0])

team_2_names = (extract_names(team_1, team_2, team_3)[1])

team_3_names = (extract_names(team_1, team_2, team_3)[2])
                        
#Function that displays statistics.  
def team_option(str, list):
    player_1, player_2, player_3, player_4, player_5, player_6 = list
    output_statement= f'''
    Team: {str} Stats:
    -------------------
    Total Players: 6
    
    Players on team:
    {player_1}, {player_2}, {player_3}, {player_4}, {player_5}, {player_6}

        '''
    return output_statement


def basketball_tool():
    print("BASKETBALL GAME STATES TOOL:")
    print("\n")
    print("----------Menu-----------")
    tool = True
    while tool:
        print("Here are your options:","\n", "A) Display Team Stats", "\n", "B) Quit")
        print("\n")
        print("\n")
        try:
            option = input("Enter an option: ")
            
            if option.isalpha() == False or len(option) >= 2 or option in ABC:
                raise ValueError("Please choose an option that is provided")
                
        except ValueError as err:
            print("Thats is not a valid response.")
            print(f"({err})")
            continue
    
        if option.lower() == 'a':
            print(f" A) {TEAMS[0]}","\n", f"B) {TEAMS[1]}", "\n", f"C) {TEAMS[2]}")
            print("\n")
            try:
                option_2 = input("Pick a team: ")
                if option_2.isalpha() == False or len(option_2) >= 2 or option_2 in ABC_2:
                    raise ValueError("You must enter a option provided.")
                    continue
    
            except ValueError as err :
                print("Thats is not a valid response.")
                print(f"({err})")
                print ("\n")
                
            if option_2.lower() == 'a':
                print(team_option(f"{TEAMS[0]}",team_1_names))
                print("\n")
                input("Press ENTER to Continue: ")
                
            elif option_2.lower()== 'b':
                print(team_option(f"{TEAMS[1]}", team_2_names))
                print("\n")
                input("Press ENTER to Continue: ")
                
            elif option_2.lower()== 'c':
                print(team_option(f"{TEAMS[2]}", team_3_names))
                print("\n")
                input("Press ENTER to Continue: ")
        
        else:
            tool = False
            
if __name__ == '__main__':
    basketball_tool()




