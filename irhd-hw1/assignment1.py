import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd
import math

# Task 2
def angle(v1, v2):
    """
    calculate angel between v1 and v2
    """
    def dotproduct(v1, v2):
        return sum((a*b) for a, b in zip(v1, v2))

    def length(v):
        return math.sqrt(dotproduct(v, v))
    
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

def min_angle(array, idx):
    """
    array in 2-D form, which include all vectors
    idx is index of one vector in array
    """
    array_without_vec = np.vstack([array[0:idx,:], array[idx+1:,:]])
    angles = [angle(array[idx], array_without_vec[i]) for i in range(len(array_without_vec))]
    res = min(angles)
    return res

def min_angles_mean(array):
    """
    array in 2-D form
    return a 1-D array with min_angle
    """
    min_angles = [min_angle(X, idx) for idx in range(X.shape[0])]
#     print(len(min_angles))
    res = np.mean(min_angles)
    return res

min_angles_means = []
n_sample = 100
dim = 100

for i in range(dim-1):
    X = np.random.rand(n_sample, i+1)
    min_mean = min_angles_mean(X)
    min_angles_means.append(min_mean)
y = range(len(min_angles_means))
plt.plot(y, min_angles_means)
plt.show()