from random import choice
#import random

answers = ["Yes!", "No!", "I don't know!"]

def give():
    return choice(answers)
    

print(give())
