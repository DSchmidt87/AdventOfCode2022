# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:23:06 2022

@author: schmi
"""

import numpy as np

box_indices = [n*4+1 for n in range(9)]
columns = dict()
for col in range(9):
    columns[col] = []
with open("input.txt") as file:
    for row in file.readlines():
        if row[1] == '1':
            break
        for col in range(9):
            cargo = row[box_indices[col]]
            if cargo != ' ':
                columns[col].append(cargo)

# Reverse ordering of list:
for col in range(9):
    columns[col] = columns[col][-1::-1]

with open("input.txt") as file:
    for row in file.readlines():
        if row[0] == 'm':
            qty = int(row.split('from')[0].split(' ')[1])
            source = int(row.split('from')[1].split('to')[0])-1
            dest = int(row.split('from')[1].split('to')[1])-1
            
            for i in range(qty):
                crate = columns[source].pop()
                columns[dest].append(crate)

print([columns[i][-1] for i in range(9)])


box_indices = [n*4+1 for n in range(9)]
columns = dict()
for col in range(9):
    columns[col] = []
with open("input.txt") as file:
    for row in file.readlines():
        if row[1] == '1':
            break
        for col in range(9):
            cargo = row[box_indices[col]]
            if cargo != ' ':
                columns[col].append(cargo)

# Reverse ordering of list:
for col in range(9):
    columns[col] = columns[col][-1::-1]

with open("input.txt") as file:
    for row in file.readlines():
        if row[0] == 'm':
            qty = int(row.split('from')[0].split(' ')[1])
            source = int(row.split('from')[1].split('to')[0])-1
            dest = int(row.split('from')[1].split('to')[1])-1
            
            moving_crates = [columns[source].pop() for i in range(qty)][-1::-1]
            [columns[dest].append(crate) for crate in moving_crates]

     
print([columns[i][-1] for i in range(9)])