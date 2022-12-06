# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:58:36 2022

@author: schmi
"""

available_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

file = open('input.txt', 'r')
priorities = dict()
i = 1
for letter in available_letters:
    priorities[letter] = i
    i=i+1

score = 0
for items in file.readlines():
    items = items[:-1] # remove \n at end of line    
    left  = items[:int(len(items)/2)]
    right = items[int(len(items)/2):]
    for i in left:
        if i in right:
            #print("{} and {} both contain {}".format(left, right, i))
            score = score + priorities[i]
            break
print("total score: {}".format(score))

# Part two
with open('input.txt', 'r') as infile:
    lines = [line for line in infile]

score = 0 
for i in range(int(len(lines)/3)):
    group_lines = lines[3*i:3*i+3]
    for letter in available_letters:
        if letter in group_lines[0] and letter in group_lines[1] and letter in group_lines[2]:
            print("{} is in all three of {}".format(letter, group_lines))
            score = score + priorities[letter]

print("Total score is {}".format(score))
        
    