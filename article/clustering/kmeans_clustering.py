from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
import seaborn as sns
import pandas as pd

x = np.random.rand(100, 50)
# print(df.head)

# kmeans = KMeans(n_clusters=5, random_state=0).fit(x)
# labels = kmeans.labels_

# inertias = []

# for i in range(1, 11):
#     kmeans = KMeans(n_clusters=i)
#     kmeans.fit(x)
#     inertias.append(kmeans.inertia_)

# plt.plot(range(1, 11), inertias, marker='o')
# plt.title('Elbow method')
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()

#model = KMeans()
#visualizer = KElbowVisualizer(model, k=(1, 12)).fit(df)
# visualizer.show()

kmeans = KMeans(n_clusters=4, init='k-means++', random_state=0).fit(x)
#sns.scatterplot(data=x, x="var1", y="var2", hue=kmeans.labels_)
# plt.show()
print(Counter(kmeans.labels_))
