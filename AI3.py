import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift
from matplotlib import style

style.use("ggplot")

my_input = np.array([[4,3],[6.5,7.5],[2.6,4],[7,8],[3.5,5],[6,9],[3,5],[6,8],
                     [3.5,3],[0.5,8],[4,4],[3,3],[3,4],[3.5,4],[3.4,3.7],[3.3,4.5],[3.8,4.3]])

my_model = MeanShift()
my_model.fit(my_input)

print("clusters center : \n", my_model.cluster_centers_)
print("labels : ", my_model.labels_)

plt.scatter(my_input[:, 0], my_input[:, 1], c=my_model.labels_)

plt.scatter(my_model.cluster_centers_[:,0], my_model.cluster_centers_[:,1], marker="x", s=250, linewidths=5)

plt.show()