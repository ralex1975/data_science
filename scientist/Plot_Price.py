import pandas as pd
import seaborn as sns
from time import strftime
import matplotlib.pyplot as plt


df = pd.read_csv('E:\IDE\scientist\HYDR_dd.csv', index_col='<DATE>', parse_dates=True)
df = df.sort_index()
dd = pd.DataFrame(df)
#print(dd)
#print(dd.columns)

frame = {}
for i in range(len(list(dd.index))):
    strokaa = round(abs(dd['<HIGH>'][i] - dd['<LOW>'][i]), 1)
    frame[dd.index[i].strftime("%Y-%m-%d")] = strokaa
data_dd_reset = dd.reset_index()

for i in range(len(list(data_dd_reset.index))):
    #print(data_dd_reset['<DATE>'][i])
    data_dd_reset['<DATE>'][i] = strftime("%Y-%m-%d")
    #print(data_dd_reset['<DATE>'][i])
#print(data_dd_reset['<DATE>'])

#рабочий график 3 линии
#data_dd_reset.plot(x="<DATE>", y=["<HIGH>", "<LOW>", "<CLOSE>"])
#plt.show()

#рабочий график 3 столба
#data_dd_reset.plot(x="<DATE>", y=["<HIGH>", "<LOW>", "<CLOSE>"], kind="bar")
#plt.show()

#Рабочая диаграмма шага цены
data_st_price = pd.DataFrame.from_dict(frame, orient='index').reset_index()
data_st_price.columns = ['DATE', 'STEP_PRICE']
sns.barplot(x="DATE", y="STEP_PRICE", data=data_st_price)
plt.show()

#new_sample_df = df.loc['20220123':'20220817', ['<CLOSE>']]
#new_sample_df.plot()
#plt.show()
