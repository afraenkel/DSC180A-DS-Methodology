
import random
import os

basedir = os.path.dirname(__file__)
datapath = os.path.join(basedir, 'data/jokes.txt')

JOKES = [x.strip() for x in open(datapath)]


def joke():
    joke1 = 'There are two kinds of data scientists:' 
    joke2 = ' (1) those who can extrapolate'
    joke3 = ' from incomplete data.'
    return  joke1 + joke2 + joke3


def random_joke():
    
    k = random.randint(0, len(JOKES))
    return JOKES[k]
    
