import numpy as np

# ---------- 1. Creating arrays ----------
a = np.array([1, 2, 3, 4, 5])
b = np.arange(0, 10, 2)  # 0 to 10, step 2
c = np.linspace(0, 1, 5)  # 5 values between 0 and 1
d = np.zeros((2, 3))      # 2x3 matrix of zeros
e = np.ones((3, 2))       # 3x2 matrix of ones
f = np.random.random((2, 2))  # 2x2 random matrix [0,1)

print("Array a:", a)
print("Array b:", b)
print("Array c:", c)
print("Zeros d:\n", d)
print("Ones e:\n", e)
print("Random f:\n", f)

# ---------- 2. Array operations ----------
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("\nAddition:", x + y)
print("Multiplication:", x * y)
print("Dot product:", np.dot(x, y))
print("Square:", x ** 2)

# ---------- 3. Universal functions ----------
arr = np.array([0, np.pi/2, np.pi])
print("\nSine values:", np.sin(arr))
print("Cosine values:", np.cos(arr))
print("Exponential:", np.exp(x))

# ---------- 4. Indexing & slicing ----------
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nOriginal 2D array:\n", arr2d)
print("First row:", arr2d[0])
print("Last column:", arr2d[:, -1])
print("Subarray (2x2):\n", arr2d[:2, :2])

# ---------- 5. Reshaping & stacking ----------
reshaped = np.arange(6).reshape(2, 3)
print("\nReshaped array:\n", reshaped)

vstacked = np.vstack([x, y])
hstacked = np.hstack([x, y])
print("Vertically stacked:\n", vstacked)
print("Horizontally stacked:", hstacked)

# ---------- 6. Statistical operations ----------
data = np.random.randint(0, 100, size=(3, 4))
print("\nRandom integer array:\n", data)
print("Mean:", np.mean(data))
print("Sum along axis 0:", np.sum(data, axis=0))
print("Max value:", np.max(data))
print("Index of min value:", np.argmin(data))

# ---------- 7. Boolean indexing ----------
mask = data > 50
print("\nData > 50:\n", data[mask])

# ---------- 8. Linear algebra ----------
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("\nMatrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix multiplication:\n", np.matmul(A, B))
print("Inverse of A:\n", np.linalg.inv(A))
print("Eigenvalues of A:", np.linalg.eigvals(A))