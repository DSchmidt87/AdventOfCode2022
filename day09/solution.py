# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:13:15 2022

@author: Dominik Schmidt
"""

import numpy as np

move = {'R': np.array([ 1, 0]), 
        'L': np.array([-1, 0]),
        'U': np.array([ 0, 1]),
        'D': np.array([ 0,-1])}

def follow(H,T):
    diff = H-T
    return T + np.sign(diff) * any(abs(diff)>1)

H = np.array([0,0])
T = np.array([0,0])
visited = np.zeros([1000,1000]) # 1000x1000 should be large enough...
with open('input.txt', 'r') as file:
    for line in file.readlines():
        d = line.split(' ')[0]
        s = int(line.split(' ')[1])
        for i in range(s):
            H = H + move[d]
            T = follow(H,T)
            visited[T[0]+500,T[1]+500] = 1 # 500,500 is center coordinade
print(sum(sum(visited)))

n_knots = 10
rope = np.zeros([n_knots,2], dtype=np.int32)
visited = np.zeros([1000,1000])
with open('input.txt', 'r') as file:
    for line in file.readlines():
        d = line.split(' ')[0]
        s = int(line.split(' ')[1])
        for i in range(s):
            rope[0,:] = rope[0,:] + move[d]
            for n in range(n_knots-1):
                rope[n+1,:] = follow(rope[n,:], rope[n+1,:])
                visited[rope[-1,0]+500,rope[-1,1]+500] = 1
print(sum(sum(visited)))


# 352 too low