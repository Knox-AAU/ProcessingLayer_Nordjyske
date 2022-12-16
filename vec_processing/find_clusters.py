from sklearn.cluster import KMeans
import numpy as np

N_CLUSTERS=30

def find_clusters(vecs, ids):
    array = np.array(vecs)
    kmeans = KMeans(n_clusters=N_CLUSTERS).fit(array)
    return labels_to_clusters(kmeans.labels_, ids)

def labels_to_clusters(labels, ids):
    clusters = []
    for doc_id, label in zip(ids, labels):
        clusters.append({'id': doc_id, 'cluster': int(label)})
    return {'n_clusters': N_CLUSTERS, 'clusters': clusters}
