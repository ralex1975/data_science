import pandas as pd
import seaborn as sns
from time import strftime
import matplotlib.pyplot as plt
import psycopg2
from sqlalchemy import create_engine


df = pd.read_csv('e:\IDE\scientist\HYDR_2021.csv', index_col='<DATE>', parse_dates=True)
df = df.sort_index()
dd = pd.DataFrame(df)
data_dd_reset = dd.reset_index()
print(data_dd_reset)
# print(dd.columns)

# заполнение словаря \|/
xx = yy = ww = zz = mm = []
i = 1
for i in range(50):
    xx.append(i)
new_frame = {'Пон' : xx, 'Втр' : yy, 'Ср' : ww, 'Чтв' : zz, 'Пят' : mm}
# заполнение закончено /|\
    
d = pd.DataFrame(new_frame)
BigFrame = pd.DataFrame(new_frame)
#BigFrame.pop('index')
BigFrame.index.name = 'id'
BigFrame.columns.name = 'item'
#print('data_dd_reset', data_dd_reset)
p = data_dd_reset[4::5]# расчет понедельника
p = p.reset_index()
f = data_dd_reset[5::5]# расчет вторника
f = f.reset_index()
с = data_dd_reset[6::5]# расчет среды
с = с.reset_index()
сh = data_dd_reset[7::5]# расчет четверга
сh = сh.reset_index()
a = data_dd_reset[3::5]# расчет пятницы
a = a.reset_index()
tt = len(a) - 1
print('fgg',tt)
i = 0

for i in range(tt):
    BigFrame['Пон'][i] = round((p['<CLOSE>'][i] - p['<OPEN>'][i]) * 100, 3)
    BigFrame['Втр'][i] = round((f['<CLOSE>'][i] - f['<OPEN>'][i]) * 100, 3)
    BigFrame['Ср'][i] = round((с['<CLOSE>'][i] - с['<OPEN>'][i]) * 100, 3)
    BigFrame['Чтв'][i] = round((сh['<CLOSE>'][i] - сh['<OPEN>'][i]) * 100, 3)
    BigFrame['Пят'][i] = round((a['<CLOSE>'][i] - a['<OPEN>'][i]) * 100, 3)
print(BigFrame)

# Запись фрейма в скуль базу \|/
engine = create_engine('postgresql://postgres:Quasar3@127.0.0.1/TEST')
BigFrame.to_sql('HYDR_2021', con=engine, if_exists='replace', index_label='id')

# Конец записи фрейма /|\

 #   data_dd_reset.rename(columns={'<VOL>': '<SPR>'}, inplace=True)
#   data_dd_reset['<SPR>'][i] = (p['<CLOSE>'][i] - p['<OPEN>'][i]) * 100

#sns.heatmap(BigFrame, annot = True, cmap= 'RdYlGn')
#plt.show()
