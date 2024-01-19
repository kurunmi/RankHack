#!/usr/bin/python3
import string
import copy


grid = ['ebadc', 'fghij', 'olmkn', 'trpqs', 'xywuv']

print (grid)
newgrid = []
for i in grid:
    newgrid.append(''.join(sorted(i)))
print(newgrid)
