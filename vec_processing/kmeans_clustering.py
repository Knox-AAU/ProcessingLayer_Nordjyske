from datetime import datetime
from sklearn.cluster import KMeans
import numpy as np

N_CLUSTERS=30

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
