import numpy as np
from numpy.linalg import inv

def random_permutation_matrix(n):
	# Create the identity matrix of size n
	matrix = np.eye(n)
	
	# Generate a random permutation
	perm = np.random.permutation(n)
	
	# Rearrange the rows according to the permutation
	matrix = matrix[perm]
	
	return matrix.tolist()

def inversa(A: list[list[int]]) -> list[list[int]]:
	try:
		return inv(np.array(A)).tolist()
	except:
		return None

def esInversaCubo(A: list[list[int]], B: list[list[int]]) -> bool:
	n = len(A)
	A = np.array(A)
	B = np.array(B)

	I = np.eye(n)

	return np.allclose(A @ B, I)


if __name__ == "__main__":
	n = 10

	for _ in range(100):
		A = random_permutation_matrix(n)
		B = inversa(A)

		R = random_permutation_matrix(n)

		# PUEDEN HABER ERRORES DE PRECISION DE PUNTO FLOTANTE
		assert esInversaCubo(A, B) == True
		assert esInversaCubo(A, R) == False

		C = [[np.random.randint(-n, n) for _ in range(n)] for _ in range(n)]
		D = inversa(C)

		R = [[np.random.randint(-n, n) for _ in range(n)] for _ in range(n)]

		assert esInversaCubo(C, D) == True
		assert esInversaCubo(C, R) == False
