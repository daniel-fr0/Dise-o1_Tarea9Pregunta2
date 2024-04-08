from random import randint

# operacion principal
# multiplica un vector 1xn por una matriz nxn
# retorna un vector 1xn en O(n^2)
def multVectorMatriz(x: list[int], A: list[list[int]]) -> list[int]:
	n = len(x)

	xA = []
	for j in range(n):
		xA.append(0)
		for k in range(n):
			xA[j] += x[k] * A[k][j]

	return xA

def esInversa(A: list[list[int]], B: list[list[int]], eps=1e-12) -> bool:
	n = len(A)
	x = [randint(0, 1) for _ in range(n)]

	# X * A * B
	xA = multVectorMatriz(x, A) # O(n^2)
	xAB = multVectorMatriz(xA, B) # O(n^2)

	# comparar si X = X * A * B, entonces B = A^-1
	for i in range(n):				# O(n)
		# if x[i] != xAB[i]:
		if abs(x[i] - xAB[i]) > eps: # para evitar errores de precision de punto flotante
			return False
	return True

# repite la funcion k veces para reducir la probabilidad de error
# la respuesta final tiene una probabilidad de error de 1/2^k
def esInversaRep(A: list[list[int]], B: list[list[int]], k: int, eps=1e-12) -> bool:
	for _ in range(k):
		if not esInversa(A, B, eps):
			return False
	return True


if __name__ == "__main__":
	from inversa import inversa

	def probando(pruebas, esperado, func, *args):
		fallas = 0
		for _ in range(pruebas):
			if func(*args) != esperado:
				fallas += 1
		print(f'\t{fallas*100//pruebas}% de fallas cuando se esperaba {esperado}')
	
	n = 3
	k = 10
	pruebas = 10
	eps = 1e-12

	R = [[randint(-10, 10) for _ in range(n)] for _ in range(n)]
	A = None
	B = None

	while not B:
		A = [[randint(-10, 10) for _ in range(n)] for _ in range(n)]
		B = inversa(A)

	print(f"{pruebas} pruebas sin repeticiones:")
	probando(10, True, esInversa, A, B, eps)
	probando(10, False, esInversa, A, R, eps)

	print(f"{pruebas} pruebas con {k} repeticiones:")
	probando(10, True, esInversaRep, A, B, k, eps)
	probando(10, False, esInversaRep, A, R, k, eps)
