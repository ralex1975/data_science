import pandas as pd
import seaborn as sns
from time import strftime
import matplotlib.pyplot as plt

df = pd.read_csv('e:\IDE\scientist\HYDR_2021.csv', index_col='<DATE>', parse_dates=True)
df = df.sort_index()
dd = pd.DataFrame(df)
# print(dd.columns)
frame = {}
data_dd_reset = dd.reset_index()
a = data_dd_reset[3::5]
a = a.reset_index()
#print(a)
# a.pop('index')
g = {}
h = u = 0
for i in range(len(a)):
    line = a['<CLOSE>'][i] - a['<OPEN>'][i]
    if line > 0:
        h += 1
    else:
        u += 1
    #g[a.index[i]] = line # запись данных
procentH = h * 100 / len(a)
procentU = u * 100 / len(a)
print('Плюсовые закрытия пятничных сессий', round(procentH), '%')
print('Распродажи пятничных сессий', round(procentU), '%')
print('Рост:', h, 'дней')
print('Падение:', u, 'дней')
# расчет понедельников
p = data_dd_reset[4::5]
p = p.reset_index()
#print(p)
t = {}
hh = uu = 0
for i in range(len(p)):
    line = p['<CLOSE>'][i] - p['<OPEN>'][i]
    if line > 0:
        hh += 1
    else:
        uu += 1
procentHH = hh * 100 / len(p)
procentUU = uu * 100 / len(p)
print('Плюсовые закрытия понедельника сессий', round(procentHH), '%')
print('Распродажи понедельника сессий', round(procentUU), '%')
print('Рост:', hh, 'дней')
print('Падение:', uu, 'дней')