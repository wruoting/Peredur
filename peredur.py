from sympy import *


def matrix_creation(n):
	'''
	param n: the number of total sheep we are starting with
	'''

	# create a matrix for the number of sheep
	m = eye(n)
	m = m.col_insert(n, zeros(n, 1))
	m[0, n] = n
	if n > 2:
		for i in range(1,n):
			m[i, i+1] = -i
			m[i, i-1] = -(n-i)
			m[i, i] = n/2
	return m 
	


print(matrix_creation(2))
