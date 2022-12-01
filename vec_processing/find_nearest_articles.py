from operator import itemgetter
from sklearn.neighbors import NearestNeighbors
import numpy as np
from vec_processing.find_topics import split_2d_list

NEAREAST_ARTS_AMOUNT = 5

def get_neareast_arts(word_vecs, neighbors):
    nearest_arts = []
    vecs, ids = split_2d_list(word_vecs)
    nbrs = NearestNeighbors(n_neighbors=neighbors, algorithm='ball_tree').fit(vecs)
    distances, indices = nbrs.kneighbors(vecs)
    for id, distance, indice in zip(ids, distances, indices):
        arr = []
        for ind, dis in zip(indice.tolist(), distance.tolist()):
            arr.append({'id': ids[ind], 'dist': dis})
        nearest_arts.append({'art_id': id, 'nearest': arr[1:neighbors]})
    return nearest_arts

def get_neareast_arts_old(word_vecs):
    nearest_arts = []
    for index, main_art in enumerate(word_vecs):
        id_main_art = word_vecs[index]['id']
        main_art_word_count = np.array(main_art['vec'])
        id_similarity = []
        for other_art in word_vecs:
            if other_art['vec'] != main_art['vec']:
                other_art_word_count = np.array(other_art['vec'])
                dist = np.linalg.norm(main_art_word_count-other_art_word_count)
                id_similarity.append([other_art['id'], dist])
                id_similarity.sort(key=itemgetter(1))
        neareast_vecs = id_similarity[0:NEAREAST_ARTS_AMOUNT]
        nearest_arts.append({'id': id_main_art, 'vec': neareast_vecs})
    return nearest_arts
