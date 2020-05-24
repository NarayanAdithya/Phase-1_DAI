import numpy as np
import pandas as pd

data=pd.read_excel('Data1_disease_pred.xlsx')

y=data['Disease Name']
data.drop('Disease Name',axis=1,inplace=True)
new=pd.get_dummies(data=data,drop_first=True)

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(new,y)
## Predict with even small differnces
## Main

Attributes=list(new.columns)

print("Hey There")
print("Let me predict your disease category")
diagnosis=[]
for x in Attributes:
    print('Do you Have '+x+'. Then enter 1.')
    diagnosis.append(int(input()))

diagnosis=np.array(diagnosis).reshape(1,-1)
print(rf.predict(diagnosis))
