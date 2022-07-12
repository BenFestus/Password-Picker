"""PASSWORD PICKER"""

import random
import string

adjectives = ['slow', 'smooth', 'rough', 'slimey', 'fast', 'slow']
nouns = ['lion', 'king', 'queen', 'panda', 'cup', 'van', 'brass']

while True:
    #Check if user wants to create password or exit
    reply = input('Do you want to create a new password? Type y/n - ')
    if reply == 'y':
        #Pick random adjective from list of adjectives
        adjective = random.choice(adjectives)
        #Pick random noun from list of nouns
        noun = random.choice(nouns)
        #Pick a random number using randrange function
        random_number = str(random.randrange(101))
        #Pick a random character from punctuation
        special_char = random.choice(string.punctuation)

        #Create random password
        random_password = adjective + noun + random_number + special_char
        #Print password
        print('Password:', random_password)
    else:
        break
