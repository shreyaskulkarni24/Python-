# -*- coding: utf-8 -*-
"""CKD_final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-5m3zkpqgqgLsucj34wpaXvd9kNpDPOp
"""

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sn
import missingno as msno
from matplotlib import pyplot as plt

import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import scipy.stats as stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# matplotlib inline
data = pd.read_csv(r"C:\Users\Dell\PycharmProjects\pythonProjectckdfinal\chronic_kidney_disease_full.csv")
#msno.matrix(data, figsize=[8, 8], fontsize=10)
msno.matrix(data)
plt.show()
msno.heatmap(data)
plt.show()
msno.dendrogram(data)
plt.show()

mapping = {'yes': 1, 'no': 0}
data = data.replace({'htn': mapping, 'pe': mapping, 'ane': mapping})
mapping1 = {'normal': 1, 'abnormal': 0}
data = data.replace({'rbc': mapping1, 'pc': mapping1})
mapping4 = {'present': 1, 'notpresent': 0}
data = data.replace({'pcc': mapping4, 'ba': mapping4})
mapping5 = {'good': 1, 'poor': 0}
data = data.replace({'appet': mapping5})
mapping6 = {'ckd': 1, 'notckd': 0, 'ckd\t': 1}
data = data.replace({'classification': mapping6})
data.dtypes
data = data.fillna(method='ffill')
data.isnull().sum()
data.rbc = data.rbc.fillna(1)
meansod = np.mean(data.sod)
data.sod = data.sod.fillna(meansod)
meanpot = np.mean(data.pot)
data.pot = data.pot.fillna(meanpot)
data.isnull().sum()
import PySimpleGUI as sg
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification









from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

Y = data.iloc[:,-1].values

print(Y)

X = data.iloc[:,0:11].values
print(X)

X_train, X_test, y_train, y_test = train_test_split(X, Y,test_size = 0.8, random_state = 0)

model = RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                       criterion='gini', max_depth=None, max_features='auto',
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=100,
                       n_jobs=None, oob_score=False, random_state=None,
                       verbose=0, warm_start=False)


model.fit(X_train,y_train)
predictions = model.predict(X)

y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
#print(accuracy_score(y_test,y_pred))

accuracy = accuracy_score(y_test,y_pred)
print(accuracy)













X, y = make_classification(n_samples=1000, n_features=11,
                           n_informative=2, n_redundant=0,
                           random_state=0, shuffle=False)
model = RandomForestClassifier(max_depth=2, random_state=0)
model = RandomForestClassifier()
model.fit(X, y)
predictions = model.predict(X)
###### ######
layout = [[sg.Text('Row 1'), sg.Text("Enter age in years")],
          [sg.Input()],
          [sg.Text('Row 2'), sg.Text("Enter blood pressure in mm/Hg")],
          [sg.Input()],
          [sg.Text('Row 3'), sg.Text("Enter sugar in nominal")],
          [sg.Input()],
          [sg.Text('Row 4'), sg.Text("Enter albumin in nominal(0-5)")],
          [sg.Input()],
          [sg.Text('Row 5'), sg.Text("Enter Serum Creatinine")],
          [sg.Input()],
          [sg.Text('Row 6'), sg.Text("Enter rbc(1-normal,0-abnormal)")],
          [sg.Input()],
          [sg.Text('Row 7'), sg.Text("Enter Bacteria(1-present,0-not present)")],
          [sg.Input()],
          [sg.Text('Row 8'), sg.Text("Enter sodium")],
          [sg.Input()],
          [sg.Text('Row 9'), sg.Text("Enter hemoglobin")],
          [sg.Input()],
          [sg.Text('Row 10'), sg.Text("Enter white blood cell count")],
          [sg.Input()],
          [sg.Text('Row 11'), sg.Text("Enter red blood cell count")],
          [sg.Input()],
          [sg.Button('Submit')]
          ]
# Create the window
window = sg.Window('CKD PREDICTION', layout)
# Display and interact with the Window
event, values = window.read()
a = values[0]
b = values[1]
c = values[2]
d = values[3]
e = values[4]
f = values[5]
g = values[6]
h = values[7]
i = values[8]
j = values[9]
k = values[10]
window.close()
##############
ex = np.array(
    [[a], [b], [c], [d], [e], [f], [g], [h], [i], [j], [k]])
# ex.shape
ex = ex.reshape(1, len(ex))
prediction = model.predict(ex)
#accuracy = metrics.accuracy_score(predictions, y)
#print(accuracy)

dflr = pd.read_csv(r'C:\Users\Dell\PycharmProjects\pythonProjectckdfinal\chronic_kidney_disease_full.csv')
data = dflr
data['class'] = data['class'].map({'ckd': 1, 'notckd': 0})
data['htn'] = data['htn'].map({'yes': 1, 'no': 0})
data['dm'] = data['dm'].map({'yes': 1, 'no': 0})
data['cad'] = data['cad'].map({'yes': 1, 'no': 0})
data['appet'] = data['appet'].map({'good': 1, 'poor': 0})
data['ane'] = data['ane'].map({'yes': 1, 'no': 0})
data['pe'] = data['pe'].map({'yes': 1, 'no': 0})
data['ba'] = data['ba'].map({'present': 1, 'notpresent': 0})
data['pcc'] = data['pcc'].map({'present': 1, 'notpresent': 0})
data['pc'] = data['pc'].map({'abnormal': 1, 'normal': 0})
data['rbc'] = data['rbc'].map({'abnormal': 1, 'normal': 0})
data['class'].value_counts()
plt.figure(figsize=(19, 19))
#sn.heatmap(data.corr(), annot=True, cmap='coolwarm')  # looking for strong correlations with "class" row
#plt.show()
data.isnull().sum()
data.shape[0], data.dropna().shape[0]
data.dropna(inplace=True)




Y = data.iloc[:,-1].values

X = data.iloc[:,0:11].values

xtrain1, xtest1, ytrain1, ytest1 = train_test_split(
        X, Y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler

sc_x = StandardScaler()
xtrain1 = sc_x.fit_transform(xtrain1)
xtest1 = sc_x.transform(xtest1)

print(xtrain1[0:11, :])

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(random_state = 0)
classifier.fit(xtrain1, ytrain1)

y_pred1 = classifier.predict(xtest1)

cm1 = confusion_matrix(ytest1,y_pred1)

print("Confusion Matrix LR : \n", cm1)
print("Accuracy lR : ", accuracy_score(ytest1, y_pred1))







X, y = make_classification(n_samples=1000, n_features=11,
                           n_informative=2, n_redundant=0,
                           random_state=0, shuffle=False)
logreg = LogisticRegression(max_iter=30)
logreg.fit(X, y)
test_pred = logreg.predict(X)
predictionn = logreg.predict(ex)
accuracy_lr = metrics.accuracy_score(test_pred, y)
#print('predictionn:: ', predictionn)

if prediction == 1 and predictionn == 1:
#if prediction == 1:
    print("ckd is positive")
    layout = [[sg.Text('Row 1'), sg.Text("Result")],
              [sg.Text('Row 2'), sg.Text("CKD is Positive")],
            #  [sg.Text('Row 3'), sg.Text("Accuracy : %s" % "{}".format(accuracy*100) + "%")],
              #####################################################################
              [sg.Text('Row 4'), sg.Text("Scr: ")],  # input scr(int)
              [sg.Input()],  # input type m/f from user (cr)
              [sg.Text('Row 5'), sg.Text("Age: ")],
              [sg.Input()],  # input type age from user(int)
              [sg.Text('Row 6'), sg.Text("Gender: { Male=1 and Female = 0 }")],
              [sg.Input()],
              [sg.Button('Calculate GFR')]
              ]

    # Create the window
    window = sg.Window('Final Result', layout)
    event, values = window.read()
    scr = values[0]
    age = values[1]
    gender = values[2]
    window.close()
    print(gender)
    global sev
    sev = '-'
    if gender == "1":
        print("enter in loop male")
        GFR = (141 * ((float(scr) / 0.9) ** (-1.209)) * (0.993 ** int(age)))
        if 60 < GFR < 89:
            sev = 'STAGE 1 MILD CKD'
        if 45 < GFR < 59:
            sev = 'STAGE 2A Moderate CKD'
        if 30 < GFR < 44:
            sev = 'STAGE 2B MODERATE CKD'
        if 15 < GFR < 29:
            sev = 'STAGE 3 SEVERE CKD'

        layout = [[sg.Text('Row 1'), sg.Text("GFR for Male")],
                  [sg.Text('Row 2'), sg.Text(GFR)],
                  [sg.Text('Row 3'), sg.Text(sev)],
                  [sg.Button('Ok')]]
        # Create the window
        window = sg.Window('Final Result', layout)
        event, values = window.read()

        window.close()

    if gender == "0":
        print("enter in loop female")
        GFR = (141 * ((float(scr) / 0.7) ** (-1.209)) * (0.993 ** int(age)))
        if 60 < GFR < 89:
            sev = 'STAGE 1 MILD CKD'
        if 45 < GFR < 59:
            sev = 'STAGE 2A Moderate CKD'
        if 30 < GFR < 44:
            sev = 'STAGE 2B MODERATE CKD'
        if 15 < GFR < 29:
            sev = 'STAGE 3 SEVERE CKD'
        layout = [[sg.Text('Row 1'), sg.Text("GFR for Female")],
                  [sg.Text('Row 2'), sg.Text(GFR)],
                  [sg.Text('Row 3'), sg.Text(sev)],
                  [sg.Button('Ok')]]
        # Create the window
        window = sg.Window('Final Result', layout)
        event, values = window.read()
        window.close()

else:
    print("ckd is negative")
    layout = [[sg.Text('Row 1'), sg.Text("Result")],
              [sg.Text('Row 2'), sg.Text("CKD is Negative")],
      #        [sg.Text('Row 3'), sg.Text("Accuracy : %s" % "{}".format(accuracy))]
              ]
    # Create the window
    window = sg.Window('Final Result', layout)
    event, values = window.read()








avg = ((accuracy_lr + accuracy) / 2)
layout = [[sg.Text('Row 1'), sg.Text("Accuracy of RF : %s" % "{}".format(accuracy*100) + "%")],
          [sg.Text('Row 2')], [sg.Text("Accuracy of LR : %s" % "{0:.3%}".format(accuracy_lr))],
          # Part 2 - The Layout
          [sg.Text('Row 3')], [sg.Text("Accuracy of Model : %s" % "{0:.3%}".format(avg))],
          [sg.Text('Row 4')], [sg.Text("...THANK YOU...")],
          [sg.Button('Ok')]]
# Create the window
window = sg.Window('Accuracy Window', layout)  # Part 3 - Window Defintion
# Display and interact with the Window
event, values = window.read()
window.close()
###############