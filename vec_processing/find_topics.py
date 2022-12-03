from sklearn.cluster import KMeans
import numpy as np

N_CLUSTERS=30

def find_topics(vecs, ids):
    array = np.array(vecs)
    kmeans = KMeans(n_clusters=N_CLUSTERS).fit(array)
    return labels_to_topics(kmeans.labels_, ids)

def labels_to_topics(labels, ids):
    topics = []
    for doc_id, label in zip(ids, labels):
        topics.append({'id': doc_id, 'topic': int(label)})
    return {'n_clusters': N_CLUSTERS, 'topics': topics}
