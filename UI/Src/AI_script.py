import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

# выгрузка таблицы в скрипт
t = pd.read_excel('final1.xlsx')
X_test = t.to_numpy()

# открытые модели
with open("client_prediction_model.pkl", 'rb') as file:
    model = pickle.load(file)

# предсказание
y_predict = model.predict(X_test)

produce = {
    "bad" : 0,
    'kinda bad' : 1,
    'not bad' : 2,
    'norm' : 3,
    'maybe' : 4,
    'good' : 5,
    'excelent' : 6,
    'very good' : 7
}

#ans = sorted([produce[i] for i in y_predict])
data = {
    "ID": t["ID"],
    "Predicted number": y_predict
    }
df = pd.DataFrame(data)
df_sorted = df.sort_values(by="Predicted number")
df_sorted.to_excel("ModelResult.xlsx")
# ans - output скрипта
