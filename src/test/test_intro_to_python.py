#Intro to Python and Github Assignment
#Kendrick Dawkins

import numpy as np


a = np.array([[1,0,0],[0,1,0],[0,0,1]])

for line in a:
    print ('  '.join(map(str, line)))
    
print("\n")


a = np.array([[1,3,3],[3,1,3],[3,3,1]])

for line in a:
    print ('  '.join(map(str, line)))

print("\n")

a = np.array([[1,3],[3,1],[3,3]])

for line in a:
    print ('  '.join(map(str, line)))
