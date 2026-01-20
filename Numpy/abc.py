
import numpy as np


# 1D Array
# arr = np.array([1,2,3,4,5])
# print(arr)

# Element Wise Square Root
# arr_sqr = arr ** 2
# print(arr_sqr)


# print(np.mean(arr))
# print(np.median(arr))
# print(np.min(arr))
# print(np.max(arr_sqr))
# print(np.sum(arr))



# 2D Array

# matrix = np.array([[22,2,3], [12,34,1], [23,45,3]])
# print(matrix)

# result =  np.dot(matrix, matrix.T) 
# print(result)



# Normalizayion

data = np.array(
    [
     [85,92,78],
     [67,86,32],
     [23,88,56],
     [88,67,99]
    ]
)

data_minmax = (data -  data.min(axis = 0)) / (data.max(axis = 0) - data.min(axis=0))
print('Data Standardized\n', np.round(data_minmax,2))


data_standard = (data - data.mean(axis = 0)) / data.std(axis = 0)
print('Data Standardized\n', np.round(data_standard,2))

