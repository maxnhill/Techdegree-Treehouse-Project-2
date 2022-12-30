import string

ABC = string.ascii_letters
ABC = list(ABC)
ABC.remove('a')
ABC.remove('b')
ABC.remove('A')
ABC.remove('B')
ABC_2 = ABC
ABC_2.remove('C')
ABC_2.remove('c')

TEAMS = [
    'Panthers',
    'Bandits',
    'Warriors',
]

PLAYERS = [{
        'name': 'Karl Saygan',
        'guardians': 'Heather Bledsoe',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Matt Gill',
        'guardians': 'Charles Gill and Sylvia Gill',
        'experience': 'NO',
        'height': '40 inches'
    },
    {   'name': 'Sammy Adams',
        'guardians': 'Jeff Adams and Gary Adams',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Chloe Alaska',
        'guardians': 'David Alaska and Jamie Alaska',
        'experience': 'NO',
        'height': '47 inches'
    },
    {
        'name': 'Bill Bon',
        'guardians': 'Sara Bon and Jenny Bon',
        'experience': 'YES',
        'height': '43 inches'
    },
    {
        'name': 'Joe Kavalier',
        'guardians': 'Sam Kavalier and Elaine Kavalier',
        'experience': 'NO',
        'height': '39 inches'
    },
    {
        'name': 'Phillip Helm',
        'guardians': 'Thomas Helm and Eva Jones',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Les Clay',
        'guardians': 'Wynonna Brown',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Sal Dali',
        'guardians': 'Gala Dali',
        'experience': 'NO',
        'height': '41 inches'
    },
    {
        'name': 'Suzane Greenberg',
        'guardians': 'Henrietta Dumas',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Jill Tanner',
        'guardians': 'Mark Tanner',
        'experience': 'YES',
        'height': '36 inches'
    },
    {
        'name': 'Arnold Willis',
        'guardians': 'Claire Willis',
        'experience': 'NO',
        'height': '43 inches'
    },
    {
        'name': 'Herschel Krustofski',
        'guardians': 'Hyman Krustofski and Rachel Krustofski',
        'experience': 'YES',
        'height': '45 inches'
    },
    {
        'name': 'Eva Gordon',
        'guardians': 'Wendy Martin and Mike Gordon',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Ben Finkelstein',
        'guardians': 'Aaron Lanning and Jill Finkelstein',
        'experience': 'NO',
        'height': '44 inches'
    },
    {
        'name': 'Joe Smith',
        'guardians': 'Jim Smith and Jan Smith',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Diego Soto',
        'guardians': 'Robin Soto and Sarika Soto',
        'experience': 'YES',
        'height': '41 inches'
    },
    {
        'name': 'Kimmy Stein',
        'guardians': 'Bill Stein and Hillary Stein',
        'experience': 'NO',
        'height': '41 inches'
    }
]

def main():
            
    def clean_constant(data):
        new_players = [] #creating new list to hold cleaned data
        for player in PLAYERS: #start loop through list of player dictionaries
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

    #Storing cleaned list in platform.
    clean_players = (clean_constant(PLAYERS))
    
    #slicing lists to create balance teams
    def pick_panthers(list):
        panthers = []
        panthers = list[0:6]
        return (panthers)


    def pick_bandits(list):
        bandits = []
        bandits = list[6:12]
        return (bandits)


    def pick_warriors(list):
        warriors = []
        warriors = list[12:18]
        return (warriors)
    
    
    #storing balanced team by team name
    team_panther = pick_panthers(clean_players)
    
    team_bandit = pick_bandits(clean_players)
    
    team_warrior = pick_warriors(clean_players)

    #Function that is supposed to extract names from list of dictionaries and store them to be displayed
    def extract_names(*args):
        panther_names = []
        bandit_names = []
        warrior_names = []
        
        for dictionary in team_panther:
            if type(dictionary) == dict:
                panther_names.append(dictionary['name'])
                
        for dictionary in team_bandit:
            if type(dictionary) == dict:
                bandit_names.append(dictionary['name'])
                
        for dictionary in team_warrior:
            if type(dictionary) == dict:
                warrior_names.append(dictionary['name'])
                
        return panther_names, bandit_names, warrior_names
    
    

    #Storing names of players in   
    panther_names = (extract_names(team_panther, team_bandit, team_warrior)[0])
    
    bandit_names = (extract_names(team_panther, team_bandit, team_warrior)[1])
    
    warrior_names = (extract_names(team_panther, team_panther, team_warrior)[2])
                           
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


    #Basketball game tool
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
            print(" A) Panthers","\n", "B) Bandits", "\n", "C) Warriors")
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
                print(team_option("Panthers",panther_names))
                print("\n")
                input("Press ENTER to Continue: ")
                
            elif option_2.lower()== 'b':
                print(team_option("Bandits",bandit_names))
                print("\n")
                input("Press ENTER to Continue: ")
                
            elif option_2.lower()== 'c':
                print(team_option("Warriors", warrior_names))
                print("\n")
                input("Press ENTER to Continue: ")
        
        else:
            tool = False
main()


