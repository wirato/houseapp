from django.shortcuts import render

from .models import Housedata , Price_of_unit_area
# Create your views here.
def index(req):
    result = 0
    X1 = 0.0
    X2 = 0.0
    X3 = 0.0
    X4 = 0.0
    X5 = 0.0
    X6 = 0.0
    if req.method == 'POST':
        X1 = float(req.POST['X1'])
        X2 = float(req.POST['X2'])
        X3 = float(req.POST['X3'])
        X4 = float(req.POST['X4'])
        X5 = float(req.POST['X5'])
        X6 = float(req.POST['X6'])

        from sklearn.svm import LinearSVC
        from sklearn.svm import SVR
        import pandas as pd
        import numpy as np
        from sklearn import utils
        from sklearn import preprocessing
        model = LinearSVC()
        svr = SVR()
        
        housedata = Housedata.objects.all()
        price_of_unit_area = Price_of_unit_area.objects.all()

        data, target = [], []
        for f in housedata:
            data.append([ f.X1, f.X2, f.X3, f.X4, f.X5, f.X6 ])
        for i in price_of_unit_area:
            target.append(i.Y)

        M = svr.fit(data, target)
        # result = M.predict([[X1, X2, X3, X4, X5, X6]])
        
        from joblib import dump, load
        dump(M, 'houseapp/houseapp.model')
        model2 = load('houseapp/houseapp.model')
        result = model2.predict([[X1, X2, X3, X4, X5, X6]])
        print(model2.predict([[X1, X2, X3, X4, X5, X6]]))  

        
    else:
        print('เขากด enter มา')
    return render(req, 'houseapp/index.html', { 
        'result': result,
        'X1': X1, 
        'X2': X2,
        'X3': X3, 
        'X4': X4, 
        'X5': X5, 
        'X6': X6, 
    })

