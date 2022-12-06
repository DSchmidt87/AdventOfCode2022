# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:46:47 2022

@author: Dominik.Schmidt
"""

import numpy as np

message = open('input.txt', 'r').readline()

def get_sequence_start(message, markerlength):
    message_list = [*message]
    for i in range(len(message_list)-markerlength):
        if len(np.unique(message_list[i:i+markerlength])) == markerlength:
            return(i+markerlength)

# Part 1
print(get_sequence_start(message, 4))

# Part 2
print(get_sequence_start(message, 14))