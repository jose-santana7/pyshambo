#roshambo but in python
import random
import time
import os

class Contestant:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.compscore = 0       

    def game_over(self):
        if self.score == 3:
            return True
        if self.compscore == 3:
            return True
        return False

    def update_score(self, winner):
        if winner:
            self.score += 1
        else: self.compscore += 1
    
    def comp_choice(self, option_list):
        option =  option_list[random.randint(0, 2)]
        return [option.get('name'), option.get('beats'), option.get('loses')]

    def user_choice(self, choice, option_list):
        for option in option_list:
            if option.get('name') == choice.lower():
                return [option.get('name'), option.get('beats'), option.get('loses')]
    
    def compare(self, user_choice, comp_choice):
        if user_choice[0] == comp_choice[2]:
            self.update_score(True)
        elif user_choice[0] == comp_choice[1]:
            self.update_score(False)

rock = {
    'name': 'rock',
    'beats': 'scissors',
    'loses': 'paper'
}
paper = {
    'name': 'paper',
    'beats': 'rock',
    'loses': 'scissors'
}
scissors = {
    'name': 'scissors',
    'beats': 'paper',
    'loses': 'rock'
}

options = [rock, paper, scissors]

os.system('cls' if os.name == 'nt' else 'clear')

name = input('Welcome to PyShambo! To start please enter you name: ')
os.system('cls' if os.name == 'nt' else 'clear')
user = Contestant(name)
print(f'Welcome {user.name}, first to three points win!')
while not user.game_over():
    print(f'   Scoreboard \n{user.name}: {user.score} | Computer: {user.compscore}')
    try:
        choice = input('Will you be throwing Rock, Paper, or Scissors? ')
        user_choice = user.user_choice(choice, options)
        comp_choice = user.comp_choice(options)
        user.compare(user_choice, comp_choice)
        print(f'{user.name} chose: {user_choice[0]} \nComputer chose: {comp_choice[0]}')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    except TypeError:
        print('That is not one of the options, please try again')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    

print(f'   Scoreboard \n{user.name}: {user.score} | Computer: {user.compscore}')
if user.score > user.compscore:
    print(f'{user.name} wins!!')
else:
    print('Computer wins!!')