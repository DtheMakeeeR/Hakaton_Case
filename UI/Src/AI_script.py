import pandas as pd
import pickle
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

# выгрузка таблицы в скрипт
t = pd.read_excel('final1.xlsx')
X_test = t.to_numpy()

# открытые модели
with open("client_prediction_model.pkl", 'rb') as file:
    model = pickle.load(file)

# предсказание
y_predict = model.predict(X_test)

# produce = {
#     "bad" : 0,
#     'kinda bad' : 1
#     'not bad' : 2,
#     'norm' : 3,
#     'maybe' : 4,
#     'good' : 5,
#     'excelent' : 6,
#     'very good' : 7
# }

#ans = sorted([produce[i] for i in y_predict])
data = {
    "ID": t["ID"],
    "Predicted number": y_predict
    }
df = pd.DataFrame(data)
df['Predicted number'] = df['Predicted number'].apply(lambda x: {'bad' : 0.9,'kinda bad' : 0.8,'not bad' : 0.7,'norm' : 0.5,'maybe' : 0.4,'good' : 0.3,'excelent' : 0.1,'very good' : 0.01}.get(x))
df = df.sort_values(by='Predicted number', ascending=False)
df = df [['ID','Predicted number']]
df.to_excel('mmodel.xlsx', index=False)
# ans - output скрипта
