import numpy as np

a = np.array([1, 3, 5, 7, 9], dtype='int8')
b = np.array([
    [2, 4],
    [6, 8],
    [10, 12]
], dtype='int16')
print(a)
print(b)
print(a.ndim)
print(b.ndim)
print(a.dtype)
print(b.dtype)
print(a.itemsize)
print(b.itemsize)
print(a.size)
print(b.size)
print(a.nbytes)
print(b.nbytes)