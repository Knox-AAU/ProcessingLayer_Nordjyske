from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

N_CLUSTERS=14

def find_topics(word_vecs):
    start_time = datetime.now()
    vecs, ids = split_2d_list(word_vecs)
    array = np.array(vecs)
    kmeans = KMeans(n_clusters=N_CLUSTERS).fit(array)
    print('Total time: ' + str(datetime.now() - start_time))
    return labels_to_topics(kmeans.labels_, ids)

def split_2d_list(word_vecs):
    vecs = []
    ids = []
    for word_vec in word_vecs:
        vecs.append(word_vec['vec'])
        ids.append(word_vec['id'])
    return vecs, ids

def labels_to_topics(labels, ids):
    topics = []
    for doc_id, label in zip(ids, labels):
        topics.append({'id': doc_id, 'topic': label})
    return topics

def test_clustering_for_range_n(array):
    start_time = datetime.now()
    intertia = []
    for i in range(1, 30):
        print("i: ", i)
        kmeans = KMeans(i)
        kmeans.fit(array)
        intertia.append(kmeans.inertia_)
        print(i + 'n clustering time: ' + str(datetime.now() - start_time))
    print('Total time: ' + str(datetime.now() - start_time))
    number_clusters = range(1, 30)
    plt.plot(number_clusters, intertia)
    plt.title('The Elbow')
    plt.xlabel('Number of clusters')
    plt.ylabel('Intertia')
    plt.show()
