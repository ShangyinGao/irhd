# team number: 8
# team member: Shangyin Gao, Hanbo Hu, Jia Hua, Siyuan Liu, Xianrui Niu

# Answer
# 
# If dimension p is very large, the angle between two randomly sampled vectors 
# is 90 degrees.
# 
# the result didn't change with the increase of sample size

import numpy as np
import matplotlib.pyplot as plt
import math
import time

# Task 2
def angle(v1, v2):
    """
    calculate angel between v1 and v2
    """
    def length(v):
        return math.sqrt(np.dot(v, v))
    
    return math.acos(np.dot(v1, v2) / (length(v1) * length(v2)))

def min_angle(array, idx):
    """
    calculate the min angle between the idx-th vector and others
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
    return a number with mean of the min_angle for each idx
    """
    min_angles = [min_angle(array, idx) for idx in range(array.shape[0])]
    res = np.mean(min_angles)
    return res

min_angles_means = []
# number of samples
n_sample = 100
# the max number of dimensions
dim = 1000
# start time
st = time.time()
for i in range(dim-1):
    # sample 100 vectors from dimension 1 to 1000
    X = np.random.rand(n_sample, i+1)*2-1
    # calcuate min_mean for each dimension
    min_mean = min_angles_mean(X)
    # build a 1-D array with i-th number min_angles_mean for i-th dimension
    min_angles_means.append(min_mean)
# end time
et = time.time()
print('the time cost is:', et-st)
# y is a idx for plot
y = range(len(min_angles_means))
# plot
plt.plot(y, min_angles_means)
plt.savefig('myfig')
plt.show()