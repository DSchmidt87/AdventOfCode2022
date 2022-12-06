# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

calories = np.zeros(1000, dtype=np.int32)
idx = 0
with open("input.txt", 'r') as file:
    for line in file.readlines():
        if line == "\n":
            idx = idx+1
        else:
            calories[idx] = calories[idx] + np.int32(line)
            
print("Elf with most calories: {0}".format(np.max(calories)))
print("Top three elves have in total: {}".format(np.sum(np.sort(calories)[-3:])))