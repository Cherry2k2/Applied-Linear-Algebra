def create_matrix(r,c):

	matrix = []

	for i in range(0,r):

		temp = []

		for j in range(0,c):

			print('enter',i,j,'th value')
			temp.append(int(input()))

		matrix.append(temp)

	return matrix

r1 = int(input('no.of rows of 1st matrix =  '))
c1 = int(input('no.of columns of 1st matrix = '))
r2 = int(input('no.of rows of 2nd matrix = '))
c2 = int(input('no.of columns of 2nd matrix = '))

print('for 1st matrix')
m1 = create_matrix(r1,c1)

print('for 2nd matrix')
m2 = create_matrix(r2,c2)

print('\ngiven matrices are \n',m1,m2)

if r1 != r2 or c1 != c2:
	print('addition (or) subraction of given matrices is not possible')

else:

	adn = []
	diff = []

	for i in range(0,r1):

		for j in range(0,c1):

			adn.append(m1[i][j]+m2[i][j])
			diff.append(m1[i][j]-m2[i][j])


	print('\naddition of given matrices is \n',adn)
	print('\ndifference between 1st and 2nd matrices is\n',diff) 

if c1 != r2:
	print('\nmultiplication of given matrices is not possible')

else:

	prod = []
	
	for i in range(0,r1):

		new_row = []

		for j in range(0,c2):

			temp = 0

			for k in range(0,r2):

				temp = temp + m1[i][k]*m2[k][j]

			new_row.append(temp)

		prod.append(new_row)
	
	print('\nmultiplication of given matrices is\n',prod) 