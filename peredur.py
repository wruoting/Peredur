from sympy import *
import numpy as np
def matrix_creation(n):
	'''
	param n: the number of total sheep we are starting with
	'''

	# create a matrix for the number of sheep
	m = eye(n)
	m = m.col_insert(n, zeros(n, 1))
	for i in range(1,n):
		m[i,i+1] = -i
		m[i,i-1] = -(n-i)
		m[i,i] = n 
	print(m) 
	



matrix_creation(6)
