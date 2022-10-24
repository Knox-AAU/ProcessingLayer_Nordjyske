import numpy as np
from scipy.spatial import distance

def find_nearest_docs(x1):
    for i in x1:
        nearest_docs = [
            
        ]
        for j in x2:
            np_array = np.array([[i][j]])
            return distance.pdist(np_array, 'euclidean')
        

test_arrays = np.random.rand(100,2000) #test arrays, 100 stk, 2000 dimensioner
#print(np.random.rand(100,2000))

for i in test_arrays:
    for j in test_arrays:
        find_nearest_docs(i)
    



sort_array = np.array([0,1,5,19,7,69,420, 1.4, 21, 12, 1])
print(np.sort(sort_array)) #Returnerer et sorteret array nemt.

print(np.array_split(sort_array, 5))


#def find_nearest_docs():
    