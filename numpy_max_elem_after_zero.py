import numpy as np
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0, 7, 0, 8, 11, 0, 4])
zero = x==0
print (x[1:][zero[:-1]].max())