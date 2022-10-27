from operator import itemgetter
import numpy as np
from scipy.spatial import distance

expected_output = [
            [
                1,
                [
                    2,
                    15.297058540778355
                ],
                [
                    3,
                    19.621416870348583
                ]
            ],
            [
                2,
                [
                    1,
                    15.297058540778355
                ],
                [
                    3,
                    11.0
                ]
            ],
            [
                3,
                [
                    1,
                    19.621416870348583
                ],
                [
                    2,
                    11.0
                ]
            ]
        ]
def skrald(e):
    return abs (e-0)
    

input_list = [[1,[1,2,3,4,5,6,7,8,9,10]],[2,[10,9,8,7,10,9,8,7,6,5]],[3,[11,11,11,11,11,11,11,11,11,11]],[4,[13,5,1,55,22,12,7,9,33,2]],[5,[31,32,29,12,9,7,7,7,0,2]],[6,[0,11,1,1,14,99,4,29,33,21]],[7,[1,0,0,0,17,15,13,11,9,7]],[8,[12,1,29,40,17,19,88,6,62,8]],[9,[55,0,8,3,3,51,55,0,0,0]],[10,[0,72,74,3,3,51,55,0,0,0]]]

i = 0
similarity_array = []
for j in input_list:
    id_main_doc = input_list[i][0]
    similarity_array.append([id_main_doc])
    arr = np.array(j[1])
    for k in input_list:
        if (k[1] != j[1]):
            arra = np.array(k[1])
            dist = np.linalg.norm(arr-arra)
            similarity_array[i].append([k[0], dist])
            
            #similarity_array[i][1][1].sort(key=skrald)
    print(similarity_array[i][1][1])
    sorted(similarity_array[i], key=similarity_array[i][1][1])
    #similarity_array[1][1].sort(key=skrald)
    #similarity_array[0].sort(key=skrald2)
    i = i + 1
#similarity_array = [item[0].split(",") for item in similarity_array]

#sorted_sim_array = sorted(similarity_array, key=itemgetter(1))
#print(sorted_sim_array)

# def fuck_det_her_fucking_fuck_lort(similarity):
#     print(similarity[1][1])
#     return similarity[1][1]

# #for m in similarity_array:
# sorted(similarity_array, key=fuck_det_her_fucking_fuck_lort)
# #similarity_array.sort(key=fuck_det_her_fucking_fuck_lort)

# print(similarity_array)
