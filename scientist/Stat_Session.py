import pandas as pd
import seaborn as sns
import calendar
import datetime
from time import strftime
import matplotlib.pyplot as plt
import re

tiker = 'HYDR_2021'
df = pd.read_csv(f'e:\IDE\scientist\{tiker}.csv', index_col='<DATE>', parse_dates=True)
df = df.sort_index()
dd = pd.DataFrame(df)
# print(dd.columns)


frame = {}
data_dd_reset = dd.reset_index()
sdf = data_dd_reset
a = data_dd_reset[3::5]
a = a.reset_index()

# расчет понедельников
p = data_dd_reset[4::5]
p = p.reset_index()
# print(p)
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

print('Плюсовые закрытия сессий понедельника', round(procentHH), '%')
print('Распродажи сессий понедельника', round(procentUU), '%')
print('Рост:', hh, 'дней')
print('Падение:', uu, 'дней', '\n', '**************')


# Поиск всех пятниц и расчет % роста и падения
value_up_fr = value_down_fr = 0
for i in range(len(sdf)):
    date_all = sdf['<DATE>'][i].strftime("%Y-%m-%d")
    date_i = datetime.datetime.strptime(date_all, '%Y-%m-%d')
    line = sdf['<CLOSE>'][i] - sdf['<OPEN>'][i]
    if pd.to_datetime(date_i).day_name() == 'Friday' and line > 0:
        value_up_fr += 1
    if pd.to_datetime(date_i).day_name() == 'Friday' and line < 0:
        value_down_fr += 1     
procent_up = value_up_fr * 100 / (value_up_fr + value_down_fr)
procent_down = value_down_fr * 100 / (value_up_fr + value_down_fr)   

# Вывод данных
print('!!Плюсовые закрытия пятничных сессий', round(procent_up), '%')
print('!!Распродажи пятничных сессий', round(procent_down), '%')
print('!!Кол-во пятниц:', value_up_fr + value_down_fr, 'дней')
print('!!Рост:', value_up_fr, 'дней')
print('!!Падение:', value_down_fr, 'дней', '\n', '**************') 
        




            




#my_date = datetime.datetime(2021, 1, 1)
#print(pd.to_datetime(my_date).day_name())