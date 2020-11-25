from __future__ import print_function
import myo as libmyo
import csv
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, precision_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn import tree
import numpy as np

import pandas as pd
libmyo.init('C:/sj/secondsem/multimedia/project/myo-sdk-win-0.9.0/bin')
c1=list()
c2=list()
c3=list()
c4=list()
c5=list()
c6=list()
c7=list()
c8=list()

class Listener(libmyo.DeviceListener):
    def on_connect(self, myo, timestamp, fwv): 
        myo.set_stream_emg(libmyo.StreamEmg.enabled)
        
    def on_emg_data(self, myo, timestamp, emg):
        global c1,c2,c3,c4,c5,c6,c7,c8
        print(emg)
        c1.append(emg[0])
        c2.append(emg[1])
        c3.append(emg[2])
        c4.append(emg[3])
        c5.append(emg[4])
        c6.append(emg[5])
        c7.append(emg[6])
        c8.append(emg[7])
        #print("done")
        
def naive():
    res = pd.read_csv('result15.csv', header=None)
#    res.columns = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7',  'e8', 'e9']
    res1 = pd.read_csv('result1.csv', header= None)
#    res1.columns = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8']
    X = res.iloc[:,0:8]
    Y = res.iloc[:,8]
    test = res1.iloc[:,0:8]
    clf = GaussianNB()
    clf.fit(X, Y)
    Y_pred = clf.predict(test)
    print(Y_pred)
    
def svmi():
    res = pd.read_csv('result15.csv', header=None)
#    res.columns = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7',  'e8', 'e9']
    res1 = pd.read_csv('result1.csv', header= None)
#    res1.columns = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8']
    X = res.iloc[:,0:8]
    Y = res.iloc[:,8]
    test = res1.iloc[:,0:8]  
    kernels = ('linear','poly','rbf')
    for index, kernel in enumerate(kernels):
        model = svm.SVC(kernel=kernel,C=1,gamma=1)
        model.fit(X, Y)
        predictions = model.predict(test)
        print("SVM(",kernel,") = ",predictions)
    
def knn():
    res = pd.read_csv('result15.csv', header=None)
#    res.columns = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7',  'e8', 'e9']
    res1 = pd.read_csv('result1.csv', header= None)
#    res1.columns = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8']
    X = res.iloc[:,0:8]
    Y = res.iloc[:,8]
    test = res1.iloc[:,0:8]
    neigh = KNeighborsClassifier(n_neighbors=40)
    neigh.fit(X, Y)
    predictions = neigh.predict(test)
    print("knn:",predictions)
    
def decision_tree():  
    res = pd.read_csv('result15.csv', header=None)
#    res.columns = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7',  'e8', 'e9']
    res1 = pd.read_csv('result1.csv', header= None)
#    res1.columns = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8']
    X = res.iloc[:,0:8]
    Y = res.iloc[:,8]
    test = res1.iloc[:,0:8]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    p=clf.predict(test)
    print("decision_tree:",p)
    
    
def main():
    x=[]
    hub = libmyo.Hub()
    listener = Listener()
    try:
        hub.run_once(5000, listener)
    finally:
        x1=0
        x2=0
        x3=0
        x4=0
        x5=0
        x6=0
        x7=0
        x8=0
        print(len(c1))
        for i in range (len(c1)):  
            x1 = x1+c1[i]
            x2 = x2+c2[i]
            x3 = x3+c3[i]
            x4 = x4+c4[i]
            x5 = x5+c5[i]
            x6 = x6+c6[i]
            x7 = x7+c7[i]
            x8 = x8+c8[i]
        print(x1,x2,x3,x4,x5,x6,x7,x8) 
        x.append(str(x1/len(c1)))
        x.append(str(x2/len(c1)))
        x.append(str(x3/len(c1)))
        x.append(str(x4/len(c1)))
        x.append(str(x5/len(c1)))
        x.append(str(x6/len(c1)))
        x.append(str(x7/len(c1)))
        x.append(str(x8/len(c1)))
        print(x1/len(c1),x2/len(c1),x3/len(c1),x4/len(c1),x5/len(c1),x6/len(c1),x7/len(c1),x8/len(c1)) 
        print(x)
        
    filename = "result1.csv"
    with open(filename, 'w', newline='') as csvfile:
            """creating a csv writer object"""
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows([x])
    hub.shutdown()  
    naive()        
    svmi()
    decision_tree()
    knn()


if __name__ == '__main__':
    main()