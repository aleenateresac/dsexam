# import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# data = pd.read_csv('grades.csv')
data = load_iris()
a = data.data
b = data.target
a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.3, train_size=0.3, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
c = knn.fit(a_train, b_train)
acc = accuracy_score(b_test, c)
print(c)
print(acc)
