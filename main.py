# import numpy as np

# import matplotlib.pyplot as plt

# def readpgm(name):

#     with open(name) as f:

#         lines = f.readlines()

#     # This ignores commented lines

#     for l in list(lines):

#         if l[0] == '#':

#             lines.remove(l)

#     # here,it makes sure it is ASCII format (P2)

#     assert lines[0].strip() == 'P5' 

#     # Converts data to a list of integers

#     data = []

#     for line in lines[1:]:

#         data.extend([int(c) for c in line.split()])

#     return (np.array(data[3:]),(data[1],data[0]),data[2])

# data = readpgm("scaled_shapes.pgm")

# plt.imshow(np.reshape(data[0],data[1])) # Usage example

def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1


print(findDuplicate([3,1,3,4,2]))