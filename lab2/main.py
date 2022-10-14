import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter matrix size (must be even and greater than 0): "))

if (n % 2) | (n < 1):
    raise Exception("The size must be even and greater than 0!")

k = int(input("Enter number multiplier: "))

A = np.random.randint(-10, 10, size=(n, n))
print("Matrix A:")
print(A)

middle = n // 2

E = A[0:middle, 0: middle]
B = A[0:middle, middle:]
D = A[middle:, 0:middle]
C = A[middle:, middle:]

print("Matrix E:")
print(E)
print("Matrix B:")
print(B)
print("Matrix D:")
print(D)
print("Matrix C:")
print(C)

F = A.copy()

numberOfRows = 0
check = True

for i in B:
    for j in i[0::2]:
        if j != 0:
            check = False
    if check:
        numberOfRows += 1

positive_matrix = np.where(B > 0, B, 0)
amount = np.sum(positive_matrix[0::2, :])

Ef = E.copy()
Cf = C.copy()

if numberOfRows > amount:
    i = 0
    for row in Ef:
        j = 0
        for value in row:
            Ef[i, j], Cf[middle - 1 - i, middle - 1 - j] = Cf[middle - 1 - i, middle - 1 - j], Ef[i, j]
            j += 1
        i += 1
    F = np.hstack([np.vstack([Ef, D]), np.vstack([B, Cf])])
else:
    F = np.hstack([np.vstack([B, D]), np.vstack([E, C])])

print("Matrix F:")
print(F)
print("Matrix A:")
print(A)

determinator = np.linalg.det(A)
print("The determinant of A:")
print(determinator)

diagonal_sum = np.trace(F)
print("The diagonal sum of F:")
print(diagonal_sum)

At = np.transpose(A)

if determinator > diagonal_sum:
    Ainv = np.linalg.inv(A)
    Finv = np.linalg.inv(F)
    result = Ainv * At - k * Finv
else:
    Ft = np.transpose(F)
    G = np.tril(A)
    result = (At + G - Ft) * k

print("Result:")
print(result)

Dgraph = plt.figure()
Dsize = len(D) * len(D[0])
x = np.linspace(0, Dsize, Dsize)
y = np.asarray(D).reshape(-1)
plt.plot(x, y)
plt.title("Matrix D")
plt.show()

Bgraph = plt.figure()
Bsize = len(B) * len(B[0])
x = np.linspace(0, Bsize, Bsize)
y = np.asarray(B).reshape(-1)
plt.plot(x, y)
plt.title("Matrix B")
plt.show()

Cgraph = plt.figure()
Csize = len(C) * len(C[0])
x = np.linspace(0, Csize, Csize)
y = np.asarray(C).reshape(-1)
plt.plot(x, y)
plt.title("Matrix C")
plt.show()



