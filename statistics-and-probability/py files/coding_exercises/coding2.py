import numpy as np

# create a numpy array
M = np.array([
 [1, 2, 3, 9],
 [2, 3, 4, 0],
 [3, 4, 5, 1],
 [8, 6, 2, 3],
])

print(M.shape)  # The shape of an array is the number of elements in each dimension (4x4)
print(M.size)  # Number of elements in the array - 16
print(M.ndim)  # number of array dimensions - 2 - it means 2 dimensional array - 2D

print(M[0])  # prints the first row in the array
print(M[0][0])  # prints the 1st element from 1st row in the array
print(M[0, 1])  # prints the element from 1st row and 2nd column

print(M[1:4, 2:4])  # Access sub matrix - 2nd to 4th row and 3rd to 4th column
print(M[1:3, :])  # 2nd to 3rd row and all the columns


a = np.arange(2, 11)  # Create an array of consecutive values
print(a)  # 1D array with numbers 2 to 10

array_steps = np.linspace(0, 1, 5)  # Create an array of consecutive values from a to b with the certain number of steps
print(array_steps)  # array with 5 numbers between 0 and 1 (included). Evenly distributed.

print(np.where(M > 3))  # prints indexes where the element is located - in case of 2D array it prints 2 separate arrays
print(np.where(a > 3))

print(a[a > 4])  # prints new array from old array, where the condition is met

print(a.reshape(3, 3))  # returns an array containing the same data with a new shap
# NB! Know the element size for reshaping

print(M.flatten())  # returns an 1D array with all the same data

print(M.diagonal())  # access the matrix diagonal

# Statistical functions
print(np.max(M))  # returns max element form the array
print(np.min(M))  # returns min element from the array
print(np.mean(M))  # returns mean value meaning - average value - adds all elements and divides with the size of array

print(np.identity(4))  # The Identity array is a square array with ones on the main diagonal
# I created 4x4 matrix

print("===================================================")

m1 = np.array([
    [1, 2, 1],
    [2, 4, 6]
])
m2 = np.array([
    [1, 1],
    [2, 3],
    [6, 1]
])

print(np.dot(m1, m2))  # Dot product
print(m1 @ m2)  # does the same thing as dot product
print(m1 + m2.reshape(2, 3))  # adding 2 array values
print(m1 - m2.reshape(2, 3))  # separates 2 array values
