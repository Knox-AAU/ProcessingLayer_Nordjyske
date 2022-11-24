from operator import itemgetter
import numpy as np

NEAREAST_DOCS_AMOUNT = 5


def get_nearest_docs(id_and_word_count_arr):
    nearest_docs_array = []
    for index, main_doc in enumerate(id_and_word_count_arr):
        id_main_doc = id_and_word_count_arr[index][0]
        nearest_docs_array.append([id_main_doc])
        main_doc_word_count = np.array(main_doc[1])
        id_similarity = []
        for other_doc in id_and_word_count_arr:
            if other_doc[1] != main_doc[1]:
                other_doc_word_count = np.array(other_doc[1])
                dist = np.linalg.norm(main_doc_word_count-other_doc_word_count)
                id_similarity.append([other_doc[0], dist])
                id_similarity.sort(key=itemgetter(1))
        nearest_docs_array[index].append(id_similarity[0:NEAREAST_DOCS_AMOUNT])
    return nearest_docs_array
