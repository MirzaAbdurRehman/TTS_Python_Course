
import numpy as np

marks = np.array([10,20,30,40,50,60,100])

print(marks[3])
print(marks[-1])
print(marks[-3])
print(marks[0:6])
print(marks[:6])
print(marks[::3])
print(marks[1::2])



students  = np.array([
    [23,45,66,77,23],  #row 0
    [13,35,65,97,93],
    [3,65,62,87,53],
    [13,42,61,7,3],    #row 3

    #col 0         #col 4
])

print(students.shape)
print(students[0])
print(students[1, 2])
print(students[:, 2])
print(students[-2:, :2])
