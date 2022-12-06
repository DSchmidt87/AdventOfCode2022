# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:27:39 2022

@author: schmi
"""
# A B C = ROCK PAPER SCISSORS
# X Y Z = ROCK PAPER SCISSORS

import numpy as np

# First index is my choice, second is enemy choice
return_points = np.array([[4,1,7],[8,5,2],[3,9,6]])

cast = {'A':0,'B':1,'C':2, 'X':0,'Y':1,'Z':2}

file = open('input.txt', 'r')
score = 0
for play in file.readlines():
    enemy = play[0]
    me = play[2]
    score = score + return_points[cast[me],cast[enemy]]
print(score)


# Part two
# A B C = ROCK PAPER SCISSORS
# X Y Z = LOSE DRAW  WIN

# First index is enemy choice, second is my choice
return_points = np.array([[3,4,8],[1,5,9],[2,6,7]])

file = open('input.txt', 'r')
score = 0
for play in file.readlines():
    enemy = play[0]
    me = play[2]
    score = score + return_points[cast[enemy],cast[me]]
print(score)