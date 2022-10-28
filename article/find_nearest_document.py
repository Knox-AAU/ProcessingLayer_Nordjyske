from operator import itemgetter
import numpy as np

NEAREAST_DOCS_AMOUNT = 5

input_list = [[1,[1,2,3,4,5,6,7,8,9,10]],[2,[10,9,8,7,10,9,8,7,6,5]],[3,[11,11,11,11,11,11,11,11,11,11]],[4,[13,5,1,55,22,12,7,9,33,2]],[5,[31,32,29,12,9,7,7,7,0,2]],[6,[0,11,1,1,14,99,4,29,33,21]],[7,[1,0,0,0,17,15,13,11,9,7]],[8,[12,1,29,40,17,19,88,6,62,8]],[9,[55,0,8,3,3,51,55,0,0,0]],[10,[0,72,74,3,3,51,55,0,0,0]]]

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
    #print(similarity_array)
    return similarity_array