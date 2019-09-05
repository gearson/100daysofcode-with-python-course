#%%
import random


class Roll:


    def __init__(self, roll=None):
        self.roll_dict = {
            'rock' : {'rock' : 'draw', 'scissors' : 'win', 'paper' : 'lose'},
            'scissors' : {'rock' : 'lose', 'scissors' : 'draw', 'paper' : 'win'},
            'paper' : {'rock' : 'win', 'scissors' : 'lose', 'paper' : 'draw'}
            }
            
        if not roll:
            self.roll = random.choice(list(self.roll_dict.keys()))
        else:
            self.roll = roll

    def can_defeat(self):
        return 

    def defeated_by(self):
        return


#%%
class Player:


    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'Player({self.name})'

    

#%%
roll_map = {
            'rock' : {'rock' : 'draw', 'scissors' : 'win', 'paper' : 'lose'},
            'scissors' : {'rock' : 'lose', 'scissors' : 'draw', 'paper' : 'win'},
            'paper' : {'rock' : 'win', 'scissors' : 'lose', 'paper' : 'draw'}
            }

roll_map['rock']['rock']

#%%
