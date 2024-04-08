# Problema
Sea $A$ y $B$ dos matrices $n \times n$, para algún entero $n > 0$.

Sospechamos que $B = A^-1$. Esto es, que $B$ es la matriz inversa de $A$.

Diseñe un algoritmo de Monte Carlo que permita confirmar esta sospecha, con un cierto
error permitido $\epsilon$, usando tiempo $O(n^2 log\frac{1}{\epsilon})$.

# Solucion
Si $B = A^-1$, entonces $A \times B = I$, donde $I$ es la matriz identidad.

Si suponemos que $B \neq A^-1$, entonces $D = A \times B - I$ es no nula.

Sea $i$ una fila en $D$ donde un elemento no es cero.

Sea $S \subseteq \{1, 2, \ldots, n\}$ un subconjunto aleatoriamente formado.

La probabilidad de que $S$ contenga a $i$ es $\frac{1}{2}$.

Luego, la suma de las filas de $D$ se puede comparar al vector $\hat 0 = \langle 0, \dots, 0 \rangle$. Si la suposicion es correcta, la suma de las filas de $D$ debe ser diferente a $\hat 0$.

Definimos $\sum_{S}(D)$ como el vector con la suma de las filas en $S$ de $D$.
- Si $\sum_{S}(D) \neq \hat 0$, entonces $B \neq A^-1$.
- Si $\sum_{S}(D) = \hat 0$, entonces $B = A^-1$ con una probabilidad de $\frac{1}{2}$. Pudimos haber tenido suerte al escoger $S$.

Para calcular $\sum_{S}(D)$ hacemos lo siguiente:
- Sea $X$ un vector de $n$ posiciones, de forma que
  - $X[i] = 1$ si $i \in S$
  - $X[i] = 0$ si $i \notin S$
- Entonces, $\sum_{S}(D) = X \times D$.
	- Por lo tanto $\sum_{S}(D) = X \times (A \times B - I) = X \times A \times B - X$.

Finalmente, como esto se quiere comparar con $\hat 0$, el problema se reduce a $X = X \times A \times B$.
- De ser cierto, podria ser que $B = A^-1$ con una probabilidad de $\frac{1}{2}$.
- De ser falso, estamos seguros que $B \neq A^-1$.

# Complejidad
Como el algoritmo consiste en multiplicar un vector $1\times n$ y dos matrices $n\times n$, si se hace primero la multiplicación con el vector se tienen dos multiplicaciones en $O(n^2)$ y luego una comparación del vector $1\times n$ resultante con otro vector $1\times n$, lo cual es $O(n)$. Y para asegurar que el resultado permita una probabilidad de error de un cierto $\epsilon > 0$, se debe iterar el mismo procedimiento una cantidad $k = log\frac{1}{\epsilon}$, por lo tanto la complejidad en tiempo finalmente es de $O(n^2 log\frac{1}{\epsilon})$.

# Implementacion
Para implementar el algoritmo, se utilizó el generador de números aleatorios de la librería `random` de Python.

Para probar el algoritmo, se requirieron funciones adicionales importadas de `numpy`.

# Como ejecutar el programa
Se debe instalar la librería `numpy` para poder ejecutar el programa.
```bash
pip install numpy
```

El programa principal esta en el archivo `main.py`. Para ejecutarlo, se debe correr el siguiente comando:
```bash
python main.py
```