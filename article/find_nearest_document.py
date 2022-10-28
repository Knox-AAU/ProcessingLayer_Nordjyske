from operator import itemgetter
import numpy as np

NEAREAST_DOCS_AMOUNT = 5

def get_neareast_docs(input):
    i = 0
    similarity_array = []
    for j in input:
        id_main_doc = input[i][0]
        similarity_array.append([id_main_doc])
        main_doc = np.array(j[1])
        id_similarity = []
        for k in input:
            if (k[1] != j[1]):
                other_doc = np.array(k[1])
                dist = np.linalg.norm(main_doc-other_doc)
                id_similarity.append([k[0], dist])
                id_similarity.sort(key=itemgetter(1))
        similarity_array[i].append(id_similarity[0:NEAREAST_DOCS_AMOUNT])
        i = i + 1
    return similarity_array
