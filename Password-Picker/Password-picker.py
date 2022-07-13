import random
import string

#List of adjectives and nouns
adjectives = ['slow', 'smooth', 'fast', 'big', 'small', 'hard', 'soft', 'long', 'short']
nouns = ['cream', 'blue', 'hollow', 'cheetah', 'france']

print('WELCOME TO PASSWORD PICKER \n')

while True:

    user_reply = input('Create new password or exit? Type y/n -- ')
    if user_reply == 'y':
        #Select random adjective from list of adjectives
        adjective = random.choice(adjectives)
        #Select random noun from list of nouns
        noun = random.choice(nouns)
        #Generate a random number from 0 to 99
        random_num = random.randrange(100)
        #Convert random num variable to string
        random_num = str(random_num)
        #Select random character from list of punctuation characters
        special_char = random.choice(string.punctuation)

        #Create the password
        password_generator = adjective + noun + random_num + special_char
        #Display password
        print('Password -', password_generator)
    else:
        break
