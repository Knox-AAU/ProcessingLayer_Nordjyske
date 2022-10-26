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

input_list = [[1,[1,2,3,4,5,6,7,8,9,10]],[2,[10,9,8,7,10,9,8,7,6,5]],[3,[11,11,11,11,11,11,11,11,11,11]],[4,[13,5,1,55,22,12,7,9,33,2]]]

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
    i = i + 1
    
print(similarity_array)
