import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import silhouette_score
from vec_processing.processing_handler import split_2d_list

MAX_N_RANGE = 50

def perform_clustering_testing(word_vecs):
    start_time = datetime.now()
    vecs, ids = split_2d_list(word_vecs)
    vec_matrix = np.array(vecs)
    find_silhouette_for_range_n(vec_matrix, MAX_N_RANGE)
    find_elbow_for_range_n(vec_matrix, MAX_N_RANGE)
    print(f'Total time: {datetime.now() - start_time}')

def find_elbow_for_range_n(array, range_n):
    start_time = datetime.now()
    intertia = []
    for i in range(1, range_n):
        kmeans = KMeans(i)
        kmeans.fit(array)
        intertia.append(kmeans.inertia_)
        print(f'{i}n clustering time: {datetime.now() - start_time}')
    print(f'Total time: {datetime.now() - start_time}')
    number_clusters = range(1, range_n)
    plt.plot(number_clusters, intertia)
    plt.title('The Elbow')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.show()

def find_silhouette_for_range_n(vecs, range_n):
    silhouette = []
    for i in range(2, range_n):
        kmeans = KMeans(i)
        kmeans.fit(vecs)
        silhouette_avg = silhouette_score(vecs, kmeans.labels_)
        silhouette.append(silhouette_avg)
        print(f'For n_clusters ={i}. The average silhouette_score is :{silhouette_avg}')
    number_clusters = range(2, range_n)
    plt.plot(number_clusters, silhouette)
    plt.title('Silhouette Score')
    plt.xlabel('Number of clusters')
    plt.ylabel('Silhouette')
    plt.show()
    return silhouette_avg
