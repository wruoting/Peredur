from sympy import *
import numpy as np


def matrix_creation(n):
	'''
	param n: the number of total sheep we are starting with
	'''

	# create a matrix for the number of sheep
	m = eye(n+1)
	m = m.col_insert(n+1, zeros(n+1, 1))
	m[0, n+1] = n
	m[n, n] = 1
	for i in range(1, n-1):
		m[i, i+1] = -i
		m[i, i-1] = -(n-i)
		m[i, i] = n
	print(m)
	return m 


def peredur(n):
	matrix = matrix_creation(n)
	rref_matrix = matrix.rref()[0]
	print(rref_matrix)
	max_array = np.zeros(n)


print(peredur(2))
