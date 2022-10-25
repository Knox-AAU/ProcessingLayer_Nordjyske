import numpy as np
from scipy.spatial import distance


# def find_nearest_docs(x):
#     for i in x:
#         id_and_vec = x[i-1]
#         nearest_document_list = [].append(id)
#         for j in x:
#             dist = np.linalg.norm(arr-arra)
#             np_array = np.array([[i][j]])
#             return distance.pdist(np_array, 'euclidean')
    
#     return expected_output
   

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


#print(find_nearest_docs(1))





#sort_array = np.array([0,1,5,19,7,69,420, 1.4, 21, 12, 1])
#print(np.sort(sort_array)) #Returnerer et sorteret array nemt.

#print(np.array_split(sort_array, 5))


input_list = [[1,[1,2,3,4,5,6,7,8,9,10]],[2,[10,9,8,7,10,9,8,7,6,5]],[3,[11,11,11,11,11,11,11,11,11,11]]]

# x = 0
# for i in input_list:
#     id_doc = input_list[x][0]
#     id_vec = input_list[x][1]
#     print(id_doc)
#     print(id_vec)
#     x=x+1
    

i = 0
j=0
similarity_array = []
while i < len(input_list):
    id_main_doc = input_list[i][0]
    similarity_array.append(id_main_doc)
    
    for j in input_list[j][1]:
        arr = j
        arra = j+1
        print(j)
        j=j+1
        #print(j+1)
        dist = np.linalg.norm(arr-arra)
        similarity_array.append(dist)
        break
        # print(input_list[i][0])
        # print(input_list[i][1])
    #print(similarity_array)
    i = i + 1

# input_list_ny = [[1],[2],3,4,5,6,7,8,9,10]
# for i in input_list_ny:
#     ##k = j+1
#     id_doc = input_list_ny[i]
#     id_vec = input_list_ny[i]
#     #id_vec = input_list[j][k]
#     print(id_doc + id_vec)
#     #print(id_vec)


#[id, [id, dist],[id, dist],[id, dist],[id, dist]]

#print(id)

#dist = np.linalg.norm(arr-arra)
#print(dist)

