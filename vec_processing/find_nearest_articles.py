from operator import itemgetter
import numpy as np

NEAREAST_ARTS_AMOUNT = 5

def get_neareast_arts(word_vecs):
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
