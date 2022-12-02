from sklearn.neighbors import NearestNeighbors
from vec_processing.find_topics import split_2d_list

def get_nearest_arts(word_vecs, neighbors):
    nearest_arts = []
    vecs, ids = split_2d_list(word_vecs)
    nbrs = NearestNeighbors(n_neighbors=neighbors+1, algorithm='ball_tree').fit(vecs)
    distances, indices = nbrs.kneighbors(vecs)
    for id, distance, indice in zip(ids, distances, indices):
        arr = []
        for ind, dis in zip(indice.tolist(), distance.tolist()):
            arr.append({'id': ids[ind], 'dist': dis})
        nearest_arts.append({'art_id': id, 'nearest': arr[1:neighbors+1]})
    return nearest_arts
