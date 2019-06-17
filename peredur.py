from sympy import *


def matrix_creation(n):
	'''
	param n: the number of total sheep we are starting with
	'''

	# create a matrix for the number of sheep
	m = eye(n+1)
	m.row_del(n)
	m = m.col_insert(n, zeros(n, 1))
	m[0, n+1] = n
	for i in range(1, n):
		m[i, i+1] = -i
		m[i, i-1] = -(n-i)
		m[i, i] = n
	return m 


print(matrix_creation(1))
