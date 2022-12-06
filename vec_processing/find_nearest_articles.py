from sklearn.neighbors import NearestNeighbors

def get_nearest_arts(vecs, art_ids, neighbors):
    nearest_arts = []
    nbrs = NearestNeighbors(n_neighbors=neighbors+1, algorithm='ball_tree').fit(vecs)
    distances, indices = nbrs.kneighbors(vecs)
    for art_id, distance, indice in zip(art_ids, distances, indices):
        pairs = []
        for index, dist in zip(indice.tolist(), distance.tolist()):
            pairs.append({'id': art_ids[index], 'dist': dist})
        nearest_arts.append({'art_id': art_id, 'nearest': pairs[1:neighbors+1]})
    return nearest_arts
