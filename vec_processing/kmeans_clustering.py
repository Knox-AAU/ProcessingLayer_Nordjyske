from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import time
from data_handler.fetch import fetch_tokens

API_URL = 'http://localhost:5501/document-data-api/'

x = fetch_tokens(API_URL, 30, 0)
# x = np.random.rand(400000, 2000)  # (antal af lister, antal af dimensioner)
print(x)

start_time = time.time()
# Find optimal amount of cluster with elbow method
# intertia = []
# for i in range(1, 10):
#     print("i: ", i)
#     kmeans = KMeans(i)
#     kmeans.fit(x)
#     temp_iter = kmeans.inertia_
#     intertia.append(temp_iter)
#     print("--- %s seconds ---" % (time.time() - start_time))
# print("--- Total time: %s seconds ---" % (time.time() - start_time))
# number_clusters = range(1, 10)
# plt.plot(number_clusters, intertia)
# plt.title('The Elbow')
# plt.xlabel('Number of clusters')
# plt.ylabel('Intertia')
# plt.show()

# Performing the K-Means clustering algorithm
# kmeans = KMeans(n_clusters=10).fit(x)
# print("--- Total time: %s seconds ---" % (time.time() - start_time))
# labels = kmeans.labels_
# print(labels)
