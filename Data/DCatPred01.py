import pandas as pd
import numpy as np

data=pd.read_excel('DataCategory_pred.xlsx')
data.drop('Disease Name',axis=1,inplace=True)

y=data['Category']
data.drop('Category',inplace=True,axis=1)
new=pd.get_dummies(data,drop_first=True)
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(new,y)

Attributes=list(data.columns)
Attributes[3]='Scalp Issues'
result={'OI':'We are still Learning','DVI':'Diarrhoea Viral Infections','RI':'Respiratory Infections','RSI':'Rashes and Skin Infections'}
print("Hey There")
print("Let me predict your disease category")
diagnosis=[]
for x in Attributes:
    print('Do you Have '+x+'. Then enter 1.')
    diagnosis.append(int(input()))

diagnosis=np.array(diagnosis).reshape(1,-1)
l=rf.predict(diagnosis)
print(result[l[0]])
