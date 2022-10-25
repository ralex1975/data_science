import pandas as pd
import datetime
from time import strftime
from sqlalchemy import create_engine


# Указание имени файла загрузки котировок(без расширения)
tiker = 'HYDR_2015-2021'
print(f'\nПроверка гипотезы:\n- повышенных покупок в понедельник\n- больших распродаж в пятницу\nОбработка акции {tiker} за год')
# Загрузка данный во ФреймДату
data_read = pd.read_csv(f'e:\IDE\scientist\{tiker}.csv', index_col='<DATE>', parse_dates=True)
data_frame = pd.DataFrame(data_read)
data_frame = data_frame.reset_index()
#print(data_frame)

        
# Запись фрейма в скуль базу \|/
engine = create_engine('postgresql://postgres:Quasar3@127.0.0.1/BigData')
data_frame.to_sql('HYDR_2015-2021', con=engine, if_exists='replace', index_label='id')
# Конец записи фрейма /|\
