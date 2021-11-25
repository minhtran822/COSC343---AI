import importlib
from os import replace
import numpy as np
from numpy.random import seed
import math

# fitness = np.array([5, 10, 19, 28, 79, 55, 3, 7, 46, 15])
# subset = np.random.randint(low=0, high=10, size=7)

# seed(1)

# a = np.array([[1,2,2,1],
#              [3,4,6,4],
#              [5,6,2,3]])

# b= np.array([[7,8,9,8],
#             [9,10,12,9],
#             [11,12,7,10]])

# c = np.array([[13,14,15,17],
#              [15,16,16,13],
#              [17,18,16,18]])

# d = np.array([[[1,2],
#             [3,4]],
            
#             [[5,6],
#             [7,8]]])

# e = np.random.random((8, 2))

# input = d.ravel()

# # for i in range(2):
# #     a[:,i] = b[:,i]
# # for i in range(2,4):
# #     a[:,i] = c[:,i]

# #print(d)
# print(e)
# print(input)

# multiply = input @ e

# print(multiply)


#subset = np.random.choice(10, 5, replace=False)
for i in range(1,5):
    print("Hi + %d" % i)