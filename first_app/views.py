from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import svm
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
import sqlite3
from sqlite3 import Error
import os

import joblib

knn=joblib.load(r"C:\Users\Nishanth kv\Desktop\mini1\first_project\models\loan_model.pkl")





def index(request):
    return render(request,'home.html')

def home(request):
    return render(request,'home.html')

def loanrec(request):
    return render(request,'index.html')

def graphs(request):
    return render(request,'graphs.html')

def bellary(request):
    return render(request,'bellary.html')

def shimoga(request):
    return render(request,'shimoga.html')

def gulbarga(request):
    return render(request,'gulbarga.html')



def predictAGRI(request):
    print (request)
    if request.method == 'POST':
        District = request.POST.get('districtval')
        Area =request.POST.get('areaval')
        Amt=request.POST.get('amountval')
        Name=request.POST.get('nameval')
        Phone_no=request.POST.get('noval')
        email=request.POST.get('mailval')
        loan=request.POST.get('loanval')
        database = r"C:\Users\Nishanth\Desktop\mini1\first_project\db"


        farmer = pd.read_excel (r'E:\Farmer wise data.xlsx')
        farmer = farmer[farmer['District']==District]
        X= farmer[['Loan amount as on 31-12-17 (In Rs. lakh)']]
        y = farmer[['Bank Name']]
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
        knn = KNeighborsClassifier(n_neighbors = 7).fit(X_train, y_train)
        accuracy = knn.score(X_test, y_test)



        context={'accuracy':accuracy}


        knn_predictions = knn.predict(X_test)
        cm = confusion_matrix(y_test, knn_predictions)

#Predicted Bank
        result = knn.predict([[1],[Amt]])
        result = result[1]
        print(result)

        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO data values(?,?,?,?,?,?,?,?)",(District,Area,Amt,Name,Phone_no,email,loan,result))

        conn.commit()


        cur.close()
        conn.close()

        context={'result':result}
        return render(request,'index.html',context)
