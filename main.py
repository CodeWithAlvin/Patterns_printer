import random

import numpy as np


def random_matrix(matrix_width,matrix_height):

	matrix=[]

	for i in range(matrix_width*matrix_height):

		matrix.append(random.randint(0,100))		

	return (matrix)


def form_dna(max_width,spacing_from_left):
	"""
	going to maximum width by for loop and then 
	it goes outside for half the iteration(spacing=max_width-i)=> 40-22 =18
	(spacing between two 1's)
	and inside for rest of others

	"""
	for i in range(max_width+1):

		if i>max_width/2:

			spacing=max_width-i

		else:

			spacing=i

			if i==max_width/2:

				spacing-=1

		if i==0 or i==max_width:

			print(f"{' '*spacing_from_left}696")

		elif (i/2)%2==0:

			print(f"{' '*(spacing_from_left-spacing)}696{'0'*(spacing*2-1)}696")

		else:
			print(f"{' '*(spacing_from_left-spacing)}696{' '*(spacing*2-1)}696")
			

if __name__ == '__main__':

	while True:
		form_dna(40,40)