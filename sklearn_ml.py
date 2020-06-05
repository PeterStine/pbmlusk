# Peter Stine
# 6/5/2020
# 

# Visualization library
import matplotlib as plt

# Sci-kit learn 
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()
x = iris.data   #train
y = iris.target #test


