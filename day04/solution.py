# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:49:07 2022

@author: schmi
"""
# Part one

file = open('input.txt', 'r')
result = 0
for line in file.readlines():
    line = line[:-1] # Remove \n at end of line
    sections = [[int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])],
             [int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])]]
    if (sections[0][0] >= sections[1][0]) and (sections[0][1] <= sections[1][1]):
        result = result+1
    elif (sections[0][0] <= sections[1][0]) and (sections[0][1] >= sections[1][1]):
        result = result+1
print(result)

# Part two
file = open('input.txt', 'r')
result = 0
for line in file.readlines():
    line = line[:-1] # Remove \n at end of line
    print(line)
    sections = [[int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])],
             [int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])]]
    if (sections[0][1] >= sections[1][0]) and sections[0][0] <= sections[1][1]:
        result = result+1
        print('overlap')
print(result)