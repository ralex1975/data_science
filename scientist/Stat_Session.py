import pandas as pd
import datetime
from time import strftime


# Указание имени файла загрузки котировок(без расширения)
tiker = 'HYDR_2021'
print(f'\nПроверка гипотезы:\n- повышенных покупок в понедельник\n- больших распродаж в пятницу\nОбработка акции {tiker} за год')
# Загрузка данный во ФреймДату
data_read = pd.read_csv(f'e:\IDE\scientist\{tiker}.csv', index_col='<DATE>', parse_dates=True)
data_frame = pd.DataFrame(data_read)
data_frame = data_frame.reset_index()

# Поиск всех понедельников и расчет % роста и падения
value_up_mo = value_down_mo = 0
for i in range(len(data_frame)):
    date_all = data_frame['<DATE>'][i].strftime("%Y-%m-%d")
    date_i = datetime.datetime.strptime(date_all, '%Y-%m-%d')
    line = data_frame['<CLOSE>'][i] - data_frame['<OPEN>'][i]
    if pd.to_datetime(date_i).day_name() == 'Monday' and line > 0:
        value_up_mo += 1
    if pd.to_datetime(date_i).day_name() == 'Monday' and line < 0:
        value_down_mo += 1     
procent_up_mo = value_up_mo * 100 / (value_up_mo + value_down_mo)
procent_down_mo = value_down_mo * 100 / (value_up_mo + value_down_mo)   

# Вывод данных по понедельнику и подтверждение\не гипотезы
line_split = '* * * * ( ͡° ͜ʖ ͡°) * * * *' # разделитель
print(f'{line_split}\nПлюсовые закрытия сессий понедельника {round(procent_up_mo)} %')
print(f'Распродажи сессий понедельника {round(procent_down_mo)} %')
#print('Рост:', value_up_mo, 'дней. Падение:', value_down_mo, 'дней')
if procent_up_mo > procent_down_mo:
    print(f'    Гипотеза подтверждена\n{line_split}')
else:
    print(f'    Гипотеза не подтверждена\n{line_split}')


# Поиск всех пятниц и расчет % роста и падения
value_up_fr = value_down_fr = 0
for i in range(len(data_frame)):
    date_all = data_frame['<DATE>'][i].strftime("%Y-%m-%d")
    date_i = datetime.datetime.strptime(date_all, '%Y-%m-%d')
    line = data_frame['<CLOSE>'][i] - data_frame['<OPEN>'][i]
    if pd.to_datetime(date_i).day_name() == 'Friday' and line > 0:
        value_up_fr += 1
    if pd.to_datetime(date_i).day_name() == 'Friday' and line < 0:
        value_down_fr += 1     
procent_up_fr = value_up_fr * 100 / (value_up_fr + value_down_fr)
procent_down_fr = value_down_fr * 100 / (value_up_fr + value_down_fr)   

# Вывод данных по пятнице и подтверждение\не гипотезы
print(f'Плюсовые закрытия пятничных сессий {round(procent_up_fr)} %')
print(f'Распродажи пятничных сессий {round(procent_down_fr)} %')
#print('Рост:', value_up_fr, 'дней. Падение:', value_down_fr, 'дней')
if procent_down_fr > procent_up_fr:
    print(f'    Гипотеза подтверждена\n{line_split}\n')
else:
    print(f'    Гипотеза не подтверждена\n{line_split}\n')
