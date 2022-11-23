from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import time

def split_2d_list(input):
    vecs = []
    ids = []
    for word_vec in input:
        vecs.append(word_vec['vec'])
        ids.append(word_vec['id'])
    return vecs, ids
    
def do_clustering(input):
    vecs, ids = split_2d_list(input)
    array = np.array(vecs)
    print(array)
    
    # x = np.random.rand(400000, 2000)  # (antal af lister, antal af dimensioner)
    start_time = time.time()
    # Find optimal amount of cluster with elbow method
    # intertia = []
    # for i in range(1, 30):
    #     print("i: ", i)
    #     kmeans = KMeans(i)
    #     kmeans.fit(array)
    #     intertia.append(kmeans.inertia_)
    #     print("--- %s seconds ---" % (time.time() - start_time))
    # print("--- Total time: %s seconds ---" % (time.time() - start_time))
    # number_clusters = range(1, 30)
    # plt.plot(number_clusters, intertia)
    # plt.title('The Elbow')
    # plt.xlabel('Number of clusters')
    # plt.ylabel('Intertia')
    # plt.show()

    # Performing the K-Means clustering algorithm
    kmeans = KMeans(n_clusters=14).fit(array)
    print("--- Total time: %s seconds ---" % (time.time() - start_time))
    labels = kmeans.labels_
    print(labels)
