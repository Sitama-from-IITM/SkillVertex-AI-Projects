import scipy
import numpy
import matplotlib
import pandas
import sklearn

# Check the versions of libraries
# Python version
import sys
print('Python:{}'.format(sys.version))
# scipy
import scipy
print('scipy:{}'.format(scipy.__version__))
# numpy
import numpy
print('numpy:{}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib:{}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas:{}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn:{}'.format(sklearn.__version__))

# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn. tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# #______________________________________________________Optional__________________________________________________________
# # shape
# print(dataset.shape)

# # head
# print(dataset.head(20))

# # descriptions
# print(dataset.describe())

# # class distribution
# print(dataset.groupby('class').size())

# # box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# pyplot.show()

# # histograms
# dataset.hist()
# pyplot.show()

# # scatter plot matrix
# scatter_matrix(dataset)
# pyplot.show()
# #______________________________________________________Optional_________________________________________________________

# Split-out test dataset
array = dataset.values
X = array[:,0:4]
y= array[:,4]
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state = 1, shuffle=True)

# #_____________________________________________________Optional_____________________________________________________________
# # Spot Check Algorithms
# models = []
# models.append(('LR',LogisticRegression(solver='liblinear',multi_class= 'ovr')))
# models.append(('KNN', KNeighborsClassifier()))
# models.append(('CART', DecisionTreeClassifier()))
# models.append(('NB', GaussianNB()))
# models.append (('SVM', SVC(gamma='auto')))

# # evaluate each model in turn
# results = []
# names = []
# for name, model in models:
#   kfold = StratifiedKFold(n_splits=10, random_state=1,shuffle =True)
#   cv_results = cross_val_score(model, X_train. Y_train, cv=kfold,scoring= 'accuracy')
#   results.append(cv_results)
#   names.append(name)
# print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# # Compare Algorithms
# pyplot.boxplot(results, labels=names)
# pyplot.title('Algorithm Comparison')
# pyplot.show()
# #_____________________________________________________Optionnal____________________________________________________________

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.ft(X_train, Y_train)
predictions = model.predict(X_test)

# Evaluate predictions
print(accuracy_score(Y_test, predictions))
print(confusion_matrix(Y_test, predictions))
print(classification_report(Y_test, predictions))