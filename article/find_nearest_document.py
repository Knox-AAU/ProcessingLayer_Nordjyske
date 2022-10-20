import numpy as np
from scipy.spatial import distance

def find_nearest_doc(x):
    return distance.pdist(x, 'euclidean')

np_array = np.array([[21,21,3,123,2,21], [213,21,213,321,213,1]])
print(find_nearest_doc(np_array))
