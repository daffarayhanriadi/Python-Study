# pip install numpy -> terminal
import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list_a = {list_a}")
# print(list_a ** 2) # ERROR!
print(f"vector_a = {vector_a}")
print(f"vector_a**2 = {vector_a ** 2}")
print(f"vector_a*5 = {vector_a * 5}")

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix_b = \n{matrix_b}")
print(f"matrix_b**2= \n{matrix_b ** 2}")

zeros_c = np.zeros((2,2))
print(f"zeros_c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"ones_d = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = \n{jumlah}")

"""
Output: 

list_a = [1, 2, 3, 4]
vector_a = [1 2 3 4]
vector_a**2 = [ 1  4  9 16]
vector_a*5 = [ 5 10 15 20]
matrix_b = 
[[1 2]
 [3 4]]
matrix_b**2= 
[[ 1  4]
 [ 9 16]]
zeros_c = 
[[0. 0.]
 [0. 0.]]
ones_d = 
[[1. 1.]
 [1. 1.]]
jumlah = 
[[ 3.  7.]
 [13. 21.]]
 
"""
