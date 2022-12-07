# -*- coding: utf-8 -*-
"""
@author: Dominik Schmidt
"""

file = open('input.txt', 'r')

filesystem = dict()
pwd = ['/']

for line in file.readlines():
    # remove \n
    line = line[:-1]
    if line[0] == '$':
        if line[2:3] == 'c':
            if line[5:] == '/':
                pwd = ['/']
            elif line[5:] == '..':
                pwd.pop()
            else:
                pwd.append("".join([line[5:], '/']))
                if "".join(pwd) not in filesystem.keys():
                    filesystem["".join(pwd)] = 0
    elif line[0].isdigit():
        size = int(line.split(' ')[0])
        filesystem["".join(pwd)] += size

totalsize = dict()
# Count size
for directory in filesystem:
    dirsize = 0
    for subdir in filesystem:
        if subdir[:len(directory)] == directory:
            dirsize += filesystem[subdir]
    totalsize[directory] = dirsize

result = 0
for directory in totalsize:
    if totalsize[directory] <= 100000:
        result += totalsize[directory]
print("***** PART ONE *****")
print("Total space of all folders < 100000:", result)

# Part two

space_total = 70000000
space_required = 30000000
space_used = sum(filesystem.values())
space_free = space_total - space_used
space_to_free = space_required - space_free
print()
print("***** PART TWO *****")
print("Total space:", space_total)
print("Space used:", space_used)
print("Space required:", space_required)
print("--> Space to free:", space_to_free)

dirs_large_enough = dict()
for d in totalsize:
    if totalsize[d] > space_to_free:
        dirs_large_enough[d] = totalsize[d]

import numpy as np
smallest_dir_large_enough = list(dirs_large_enough.keys())[np.argmin(list(dirs_large_enough.values()))]
print("==> Delete", smallest_dir_large_enough, "with size", dirs_large_enough[smallest_dir_large_enough])
