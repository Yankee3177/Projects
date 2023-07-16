import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.cluster import KMeans
from matplotlib import style

style.use("ggplot")

X = np.array([[3, 2],
              [6, 6],
              [2.6, 3],
              [7, 8],
              [3.5, 5],
              [6, 11]])

Y = [0, 1, 0, 1, 0, 1]

my_clf = svm.SVR(kernel='linear', C=1.0)
my_clf.fit(X, Y)

my_clf2 = KMeans(n_clusters=2)
my_clf2.fit(X)

print("SVR predict[0.5,0.8] : ", my_clf.predict([[0.5, 0.8]]))
print("SVR predict[8.5,10] : ", my_clf.predict([[8.5, 10]]))

print("SVC predict[0.5,0.8] : ", my_clf2.predict([[0.5, 0.8]]))
print("SVC predict[8.5,10] : ", my_clf2.predict([[0.6, 10]]))

plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.scatter(0.5, 0.8, c="r")
plt.scatter(8.5, 10, c="r")
plt.show()
