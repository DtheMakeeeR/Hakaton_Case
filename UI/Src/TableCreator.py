from functools import reduce
from sys import argv
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.graph_objects as go
script, path1, path2, path3, path4, path5, path6, path7, path8, path9, path10 = argv
t_v = pd.read_excel(path1)
t_int = pd.read_excel(path2).fillna(0)
t_Vladimir = pd.read_excel(path3).fillna(0)
t_Kirov = pd.read_excel(path4).fillna(0)
t_NN = pd.read_excel(path5).fillna(0)
t_Mar = pd.read_excel(path6).fillna(0)
t_Mor = pd.read_excel(path7).fillna(0)
t_Tat = pd.read_excel(path8).fillna(0)
t_Udm = pd.read_excel(path9).fillna(0)
t_Huv = pd.read_excel(path10).fillna(0)
columns = t_v.columns[5:]
t_Vladimir = t_Vladimir[['ID','Размер компании.Наименование','Карточка клиента (внешний источник).Индекс финансового риска Описание','Госконтракты.Контракт']]
t_Kirov = t_Kirov[['ID','Размер компании.Наименование','Карточка клиента (внешний источник).Индекс финансового риска Описание','Госконтракты.Контракт']]
t_NN = t_NN[['ID','Размер компании.Наименование','Карточка клиента (внешний источник).Индекс финансового риска Описание','Госконтракты.Контракт']]
t_Mar = t_Mar[['ID','Размер компании.Наименование','Карточка клиента (внешний источник).Индекс финансового риска Описание','Госконтракты.Контракт']]
t_Mor = t_Mor[['ID','Размер компании.Наименование','Карточка клиента (внешний источник).Индекс финансового риска Описание','Госконтракты.Контракт']]
t_Tat = t_Tat[['ID','Размер компании.Наименование','Карточка клиента (внешний источник).Индекс финансового риска Описание','Госконтракты.Контракт']]
t_Udm = t_Udm[['ID','Размер компании.Наименование','Карточка клиента (внешний источник).Индекс финансового риска Описание','Госконтракты.Контракт']]
t_Huv = t_Huv[['ID','Размер компании.Наименование','Карточка клиента (внешний источник).Индекс финансового риска Описание','Госконтракты.Контракт']]
t_int = t_int[['ID','Вероятность сделки, %']]
t_int = t_int[['ID', 'Вероятность сделки, %']].groupby('ID').max()
t_int['Параметр вероятности сделки'] = t_int['Вероятность сделки, %'] / 100
t_int = t_int.reset_index()[['ID', 'Параметр вероятности сделки']]
risk_map = {
    'Низкий риск': 1,
    'Средний риск': 0.5,
    'Высокий риск': 0,
}
param3_weight = 0.5
bis = {
    'Микробизнес': 0,
    'Малый бизнес': 0.3,
    'Средний бизнес': 0.6,
    'Крупный бизнес': 1,
}

t_Vladimir['Параметр бизнеса'] = t_Vladimir['Размер компании.Наименование'].apply(lambda x: bis.get(x, 0))
t_Vladimir['Параметр риска'] = t_Vladimir['Карточка клиента (внешний источник).Индекс финансового риска Описание'].apply(lambda x: risk_map.get(x, 0))
t_Vladimir['Параметр госконтракта'] = t_Vladimir['Госконтракты.Контракт'].apply(lambda x: int(x != 0) * param3_weight)
t_Vladimir = t_Vladimir[['ID', 'Параметр бизнеса', 'Параметр риска', 'Параметр госконтракта']]

t_Kirov['Параметр бизнеса'] = t_Kirov['Размер компании.Наименование'].apply(lambda x: bis.get(x, 0))
t_Kirov['Параметр риска'] = t_Kirov['Карточка клиента (внешний источник).Индекс финансового риска Описание'].apply(lambda x: risk_map.get(x, 0))
t_Kirov['Параметр госконтракта'] = t_Kirov['Госконтракты.Контракт'].apply(lambda x: int(x != 0) * param3_weight)
t_Kirov = t_Kirov[['ID', 'Параметр бизнеса', 'Параметр риска', 'Параметр госконтракта']]

t_NN['Параметр бизнеса'] = t_NN['Размер компании.Наименование'].apply(lambda x: bis.get(x, 0))
t_NN['Параметр риска'] = t_NN['Карточка клиента (внешний источник).Индекс финансового риска Описание'].apply(lambda x: risk_map.get(x, 0))
t_NN['Параметр госконтракта'] = t_NN['Госконтракты.Контракт'].apply(lambda x: int(x != 0) * param3_weight)
t_NN = t_NN[['ID', 'Параметр бизнеса', 'Параметр риска', 'Параметр госконтракта']]

t_Mar['Параметр бизнеса'] = t_Mar['Размер компании.Наименование'].apply(lambda x: bis.get(x, 0))
t_Mar['Параметр риска'] = t_Mar['Карточка клиента (внешний источник).Индекс финансового риска Описание'].apply(lambda x: risk_map.get(x, 0))
t_Mar['Параметр госконтракта'] = t_Mar['Госконтракты.Контракт'].apply(lambda x: int(x != 0) * param3_weight)
t_Mar = t_Mar[['ID', 'Параметр бизнеса', 'Параметр риска', 'Параметр госконтракта']]

t_Mor['Параметр бизнеса'] = t_Mor['Размер компании.Наименование'].apply(lambda x: bis.get(x, 0))
t_Mor['Параметр риска'] = t_Mor['Карточка клиента (внешний источник).Индекс финансового риска Описание'].apply(lambda x: risk_map.get(x, 0))
t_Mor['Параметр госконтракта'] = t_Mor['Госконтракты.Контракт'].apply(lambda x: int(x != 0) * param3_weight)
t_Mor = t_Mor[['ID', 'Параметр бизнеса', 'Параметр риска', 'Параметр госконтракта']]

t_Tat['Параметр бизнеса'] = t_Tat['Размер компании.Наименование'].apply(lambda x: bis.get(x, 0))
t_Tat['Параметр риска'] = t_Tat['Карточка клиента (внешний источник).Индекс финансового риска Описание'].apply(lambda x: risk_map.get(x, 0))
t_Tat['Параметр госконтракта'] = t_Tat['Госконтракты.Контракт'].apply(lambda x: int(x != 0) * param3_weight)
t_Tat = t_Tat[['ID', 'Параметр бизнеса', 'Параметр риска', 'Параметр госконтракта']]

t_Udm['Параметр бизнеса'] = t_Udm['Размер компании.Наименование'].apply(lambda x: bis.get(x, 0))
t_Udm['Параметр риска'] = t_Udm['Карточка клиента (внешний источник).Индекс финансового риска Описание'].apply(lambda x: risk_map.get(x, 0))
t_Udm['Параметр госконтракта'] = t_Udm['Госконтракты.Контракт'].apply(lambda x: int(x != 0) * param3_weight)
t_Udm = t_Udm[['ID', 'Параметр бизнеса', 'Параметр риска', 'Параметр госконтракта']]

t_Huv['Параметр бизнеса'] = t_Huv['Размер компании.Наименование'].apply(lambda x: bis.get(x, 0))
t_Huv['Параметр риска'] = t_Huv['Карточка клиента (внешний источник).Индекс финансового риска Описание'].apply(lambda x: risk_map.get(x, 0))
t_Huv['Параметр госконтракта'] = t_Huv['Госконтракты.Контракт'].apply(lambda x: int(x != 0) * param3_weight)
t_Huv = t_Huv[['ID', 'Параметр бизнеса', 'Параметр риска', 'Параметр госконтракта']]

t_v_1 = t_v.groupby('ID').sum()[columns].reset_index()
t_v_1['Параметр активности'] = t_v_1.apply(lambda x: int(any([x[i] != 0 for i in t_v_1.columns[-13:]])), axis=1)
t_v_1 = t_v_1[['ID', 'Параметр активности']]
ans = pd.DataFrame()
ans['ID'] = sorted(list(set(t_v['ID'])))
ans['Параметр изменения перевозок'] = [0] * len(ans)
ans = ans.set_index('ID')
t_ = t_v.values.tolist()
ans_ = ans.to_dict()['Параметр изменения перевозок']
col = t_v.columns[5:]
for i in t_:
    temp = i[5]
    for j in range(1, len(col)):
        ans_[i[0]] += (i[5+j] - temp) / 4
        if (ans_[i[0]]<0):
            ans_[i[0]]=0
        temp = i[5+j]
ans = pd.DataFrame(ans_.items(), columns = ['ID', 'Параметр изменения перевозок'])
q = ans['Параметр изменения перевозок'].max()
ans['Параметр изменения перевозок'] = ans['Параметр изменения перевозок'] / q
dfs = [t_Vladimir,t_Kirov,t_NN,t_Mar,t_Mor,t_Tat,t_Udm,t_Huv]
result = pd.concat(dfs)
result = result.drop_duplicates(subset='ID', keep='first').fillna(0)

dfs = [result, ans, t_v_1, t_int]
df_final = reduce(lambda left, right: pd.merge(left, right, on='ID', how='outer'), dfs).fillna(0)
df_final['Сумма параметров'] = df_final['Параметр бизнеса'] + df_final['Параметр риска'] + df_final['Параметр госконтракта'] + df_final['Параметр изменения перевозок'] + df_final['Параметр активности'] + df_final['Параметр вероятности сделки']
df_final.to_excel('final1.xlsx', index=False)
df_final=df_final.loc[(df_final['Сумма параметров']==0.0)]