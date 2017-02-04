"""1. Picking a random word from a text file"""

import random
import sys

def random():
    """the open statement can have any text file, apparently it is 'sowpods.txt' """
    
    with open('sowpods.txt', 'r') as f:
        """ 'r' refers to "read given file". """
        word = f.readline()
        print(random.choice(word).strip())

random()

"""2. Reading from a text file and appending it to a dictionary"""

dict = {}
    """ the open statement can have any text file, apparently it is 'Names.txt' """
with open('Names.txt') as f:
    line = f.readlines()
    while line:
        line = line.strip()
        if line in dict:
            dict[line] += 1
        else:
            dict[line] -= 1
            line = f.readline()
