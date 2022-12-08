# -*- coding: utf-8 -*-
"""
@author: Dominik Schmidt
"""

import numpy as np

idx = 0
with open('input.txt', 'r') as file:
    trees = np.array([[int(x) for x in line[:-1]] for line in file.readlines()])

visible = np.zeros(trees.shape)

for i in range(len(trees)):
    for j in range(len(trees)):
        visible_row = all(trees[i,:j] < trees[i,j]) or all(trees[i,j+1:] < trees[i,j])
        visible_col = all(trees[:i,j] < trees[i,j]) or all(trees[i+1:,j] < trees[i,j])
        visible[i,j] = visible_row or visible_col
        
# No need to adjust the edges since all([]) is True
print(sum(sum(visible)))

# Part two
scenic_scores = np.zeros(trees.shape)
for i in range(len(trees)):
    for j in range(len(trees)):
        d_left = np.where(trees[i,:j] >= trees[i,j])[0]
        if len(d_left) == 0:
            d_left = j
        else:
            d_left = j - d_left[-1]
            
        d_right = np.where(trees[i,j+1:] >= trees[i,j])[0]
        if len(d_right) == 0:
            d_right = trees.shape[1] - j - 1
        else:
            d_right = d_right[0] + 1
            
        d_up = np.where(trees[:i,j] >= trees[i,j])[0]
        if len(d_up) == 0:
            d_up = i
        else:
            d_up = i - d_up[-1]
            
        d_down = np.where(trees[i+1:,j] >= trees[i,j])[0]
        if len(d_down) == 0:
            d_down = trees.shape[0] - i - 1
        else:
            d_down = d_down[0] + 1
        scenic_scores[i,j] = d_left*d_right*d_up*d_down

print(np.max(scenic_scores))