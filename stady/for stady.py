import calendar
import datetime
from distutils.log import info
from lib2to3.pgen2.token import DEDENT
from tkinter import ttk
import pandas as pd
from collections import deque
from collections import defaultdict



# print(calendar.calendar(2021, 2, 2, 6, 3))
c = calendar.TextCalendar()
#c.prmonth(2021, 1)

my_date = datetime.datetime(2021, 1, 1)
#print(pd.to_datetime(my_date).day_name())



from collections import OrderedDict


temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5),
        ('2004', -8.2), ('2005', -1.6), ('2006', -5.9), ('2007', -2.4),
        ('2008', -1.7), ('2009', -3.5), ('2010', -12.1), ('2011', -5.8),
        ('2012', -4.9), ('2013', -6.1), ('2014', -6.9), ('2015', -2.7),
        ('2016', -11.2), ('2017', -3.9), ('2018', -2.9), ('2019', -6.5),
        ('2020', 1.5)]
#tempsr = OrderedDict(sorted(temps, key=lambda x: x[1]))
dd = deque(temps)
dd_sort = sorted(dd, key=lambda x: x[1])
dd_sort.reverse()
ordered_client_ages = OrderedDict(dd_sort)
#print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Maria', 20), ('Nikita', 18)])


rr = [6, 18, 4, 7, 8, 8, 5, 18, 12, 17, 13, 15, 6, 7, 9, 17, 18, 8, 4, 11, 10, 8, 2, 10, 6, 10, 10, 9]

def brackets(line):
    stek = deque(line)
    open_stek = stek.count('(')
    close_stek = stek.count(')')
    if open_stek == close_stek or line == "":
        return True
    else:
        return False
    
#print(brackets("(()())"))


from collections import defaultdict
from collections import Counter
from collections import OrderedDict


north = [['Milk', 'Milk', 'Beer'], ['Chocolate', 'Bread', 'Chips'], ['Cola', 'Cola', 'Yoghurt', 'Soap', 'Beer', 'Chips', 'Milk'], ['Soap', 'Soap', 'Cola', 'Cola', 'Chips'], ['Milk', 'Beer', 'Meat', 'Ketchup', 'Cola', 'Cola', 'Chips', 'Chips', 'Cola', 'Cola'], ['Beer', 'Bread', 'Bread', 'Beer', 'Beer', 'Beer', 'Bread', 'Cheese'], ['Yoghurt', 'Beer', 'Chips', 'Milk', 'Soap', 'Cola', 'Cola', 'Cola', 'Beer', 'Cola', 'Cola', 'Cola', 'Beer', 'Ketchup', 'Beer', 'Beer', 'Beer', 'Soap'], ['Milk', 'Cola', 'Cola', 'Beer', 'Beer', 'Bread', 'Bread', 'Soap', 'Cola', 'Cola', 'Beer', 'Meat', 'Bread', 'Chips'], ['Beer', 'Beer', 'Beer', 'Chips', 'Milk', 'Cola', 'Chocolate', 'Beer', 'Chocolate', 'Beer', 'Beer', 'Cola', 'Meat', 'Yoghurt', 'Beer'], ['Bread'], ['Chocolate', 'Beer', 'Meat', 'Yoghurt'], ['Cola', 'Beer', 'Beer', 'Beer', 'Chocolate', 'Beer', 'Soap', 'Beer', 'Chips', 'Soap', 'Chocolate', 'Bread', 'Chips', 'Cola', 'Bread', 'Beer', 'Cola', 'Bread'], ['Chips', 'Cola', 'Beer', 'Chips', 'Cola', 'Cola', 'Beer', 'Soap', 'Yoghurt', 'Yoghurt', 'Cola', 'Bread', 'Beer', 'Chocolate', 'Chips', 'Bread', 'Beer', 'Bread'], ['Cola', 'Chocolate'], ['Chocolate', 'Cola', 'Meat', 'Cola', 'Ketchup', 'Cola', 'Chocolate', 'Bread', 'Chocolate', 'Chocolate', 'Meat'], ['Bread', 'Milk', 'Chips', 'Ketchup', 'Cola', 'Cola', 'Cola', 'Beer', 'Beer', 'Soap', 'Beer', 'Cola'], ['Yoghurt', 'Milk', 'Soap', 'Bread', 'Cola', 'Cola', 'Milk', 'Bread', 'Chips', 'Cheese', 'Milk', 'Yoghurt', 'Bread', 'Yoghurt'], ['Cola', 'Ketchup'], ['Cola', 'Yoghurt', 'Bread', 'Cola', 'Cola', 'Chips', 'Yoghurt', 'Milk', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Cola', 'Bread', 'Beer', 'Beer', 'Cheese'], ['Beer', 'Cheese', 'Ketchup', 'Beer'], ['Beer', 'Beer', 'Beer'], ['Soap', 'Beer', 'Beer', 'Chocolate', 'Cola', 'Chocolate', 'Bread', 'Beer', 'Milk', 'Bread', 'Beer', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Cheese', 'Beer', 'Cola', 'Soap', 'Yoghurt'], ['Beer', 'Chocolate'], ['Cola', 'Beer'], ['Yoghurt', 'Beer', 'Yoghurt', 'Yoghurt', 'Chips', 'Meat', 'Beer', 'Chocolate', 'Cola', 'Cola', 'Chips', 'Bread'], ['Cola', 'Cola', 'Cola', 'Cola', 'Cola', 'Bread', 'Chips', 'Soap', 'Cola', 'Chocolate', 'Beer', 'Beer'], ['Beer', 'Cola', 'Cola', 'Bread', 'Soap', 'Beer', 'Meat', 'Beer', 'Beer', 'Beer', 'Cola', 'Chips', 'Beer', 'Cola', 'Cola', 'Bread', 'Cheese', 'Beer'], ['Cola', 'Cola', 'Ketchup', 'Beer', 'Yoghurt', 'Bread'], ['Chips', 'Yoghurt', 'Cola', 'Cola', 'Cola', 'Chocolate', 'Chips', 'Bread', 'Chocolate', 'Yoghurt', 'Chocolate', 'Milk', 'Bread', 'Bread', 'Soap', 'Milk', 'Soap', 'Cola', 'Bread', 'Beer'], ['Beer', 'Beer', 'Ketchup', 'Cola', 'Beer', 'Bread', 'Beer', 'Cola', 'Beer', 'Chocolate'], ['Beer', 'Chocolate', 'Cola', 'Beer', 'Yoghurt', 'Milk', 'Bread', 'Cheese', 'Yoghurt', 'Beer', 'Cola', 'Yoghurt', 'Cola', 'Soap', 'Beer', 'Bread', 'Meat', 'Bread', 'Cola'], ['Beer', 'Cola', 'Chips', 'Cola'], ['Cola', 'Cola', 'Beer', 'Cheese'], ['Bread', 'Soap', 'Ketchup', 'Chocolate', 'Beer', 'Cola', 'Chocolate', 'Cola', 'Cola', 'Yoghurt', 'Beer', 'Bread', 'Cola', 'Ketchup', 'Beer'], ['Bread'], ['Bread', 'Beer', 'Yoghurt', 'Yoghurt', 'Bread', 'Milk', 'Soap', 'Meat', 'Bread', 'Beer', 'Cola', 'Milk', 'Milk', 'Bread', 'Beer', 'Cola', 'Ketchup', 'Cola'], ['Bread', 'Beer', 'Bread', 'Yoghurt', 'Beer', 'Bread', 'Cola', 'Cola', 'Cola', 'Beer', 'Bread', 'Milk', 'Chips', 'Cola', 'Beer', 'Bread', 'Soap', 'Bread', 'Yoghurt', 'Bread'], ['Yoghurt', 'Beer', 'Cola', 'Beer', 'Beer', 'Beer'], ['Chips', 'Chocolate', 'Soap', 'Chocolate', 'Cola', 'Bread', 'Beer', 'Cola', 'Beer', 'Ketchup', 'Chocolate', 'Ketchup', 'Ketchup', 'Cheese', 'Chips', 'Beer', 'Chips', 'Chocolate'], ['Bread', 'Cola', 'Cola', 'Beer', 'Bread', 'Bread', 'Beer', 'Chocolate', 'Bread', 'Cola', 'Milk', 'Chips', 'Meat', 'Beer', 'Beer', 'Soap', 'Bread'], ['Beer', 'Beer', 'Bread', 'Chips', 'Beer', 'Bread', 'Bread', 'Chips', 'Beer'], ['Yoghurt', 'Bread', 'Cola', 'Bread', 'Cola', 'Bread', 'Meat', 'Cola', 'Bread', 'Beer', 'Soap', 'Chips'], ['Bread', 'Beer'], ['Milk', 'Beer', 'Meat', 'Cola', 'Beer', 'Cola', 'Cola'], ['Beer', 'Chips', 'Yoghurt', 'Beer', 'Cola', 'Beer', 'Cola', 'Cola', 'Soap', 'Cola'], ['Bread', 'Cola', 'Cola', 'Meat'], ['Cola', 'Chocolate', 'Meat', 'Beer', 'Cola', 'Bread', 'Chips', 'Beer', 'Chips', 'Chips', 'Cola'], ['Bread', 'Cola', 'Cola', 'Cola', 'Beer', 'Cola', 'Yoghurt', 'Beer', 'Chips', 'Cola', 'Chocolate', 'Chips', 'Cola', 'Cola', 'Cola', 'Cola', 'Bread', 'Cola'], ['Cola', 'Soap', 'Cola'], ['Soap', 'Chips', 'Cola', 'Beer', 'Bread', 'Soap', 'Cheese', 'Bread', 'Beer', 'Chocolate']]
center = [['Meat', 'Beer', 'Soap', 'Beer', 'Cheese', 'Cola', 'Milk', 'Soap', 'Cola', 'Meat', 'Bread', 'Chocolate', 'Chips'], ['Soap', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Beer', 'Cheese', 'Cheese', 'Beer', 'Chips', 'Chocolate', 'Chips', 'Cheese', 'Bread', 'Cola', 'Cola', 'Beer'], ['Cola', 'Soap', 'Bread', 'Milk', 'Beer', 'Meat', 'Bread', 'Bread'], ['Ketchup', 'Beer', 'Ketchup', 'Chocolate', 'Milk', 'Milk', 'Bread', 'Beer'], ['Beer', 'Beer', 'Meat', 'Ketchup', 'Soap', 'Bread', 'Cola', 'Beer'], ['Meat', 'Bread', 'Milk', 'Cheese', 'Soap', 'Beer', 'Milk', 'Cheese', 'Cola', 'Beer', 'Chips', 'Bread', 'Ketchup', 'Chocolate', 'Bread', 'Milk'], ['Yoghurt'], ['Beer', 'Milk', 'Chips', 'Soap', 'Chips', 'Milk', 'Beer', 'Chips', 'Bread', 'Meat', 'Milk'], ['Yoghurt', 'Beer', 'Cola', 'Cola', 'Beer', 'Soap', 'Cheese', 'Soap', 'Bread', 'Cola', 'Yoghurt', 'Ketchup', 'Beer', 'Milk'], ['Milk', 'Cola', 'Bread', 'Cola', 'Bread', 'Beer', 'Beer', 'Beer'], ['Yoghurt', 'Cola'], ['Bread', 'Yoghurt', 'Chips', 'Ketchup', 'Meat', 'Bread', 'Beer', 'Yoghurt', 'Cola', 'Cola'], ['Chips', 'Chocolate', 'Chips', 'Meat', 'Bread', 'Cheese', 'Bread', 'Yoghurt'], ['Ketchup', 'Soap', 'Chocolate', 'Bread'], ['Chips', 'Beer', 'Chips', 'Cola', 'Cheese', 'Soap', 'Ketchup', 'Meat', 'Cola', 'Chips', 'Beer', 'Chocolate', 'Beer', 'Milk', 'Bread', 'Ketchup', 'Chips', 'Cheese', 'Ketchup'], ['Beer', 'Milk', 'Soap', 'Chips', 'Soap', 'Bread', 'Bread', 'Milk', 'Beer'], ['Cola', 'Chips', 'Meat', 'Cola', 'Beer', 'Chocolate', 'Bread', 'Bread', 'Chips', 'Soap', 'Chocolate', 'Chips', 'Beer'], ['Meat', 'Cola', 'Chips', 'Bread', 'Chips', 'Chocolate', 'Bread', 'Meat', 'Bread', 'Yoghurt', 'Cheese', 'Bread', 'Chips', 'Cola'], ['Chips', 'Cheese', 'Bread', 'Beer', 'Bread', 'Chips', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Chocolate', 'Chocolate', 'Bread', 'Meat', 'Chips'], ['Bread', 'Milk', 'Bread', 'Cheese', 'Bread', 'Cheese', 'Ketchup', 'Beer', 'Cheese', 'Cola', 'Milk', 'Milk', 'Bread', 'Beer', 'Bread', 'Chips'], ['Yoghurt'], ['Bread', 'Bread', 'Chips', 'Cheese', 'Bread', 'Beer', 'Cola', 'Ketchup', 'Bread', 'Chips', 'Chocolate', 'Meat', 'Milk', 'Beer', 'Milk', 'Cheese', 'Bread', 'Meat', 'Bread', 'Cola'], ['Bread', 'Meat', 'Meat', 'Milk', 'Chips', 'Soap', 'Yoghurt', 'Chips', 'Beer', 'Yoghurt'], ['Bread', 'Soap', 'Bread', 'Cola', 'Bread'], ['Cola', 'Bread', 'Meat', 'Cola', 'Meat', 'Chocolate', 'Chips', 'Meat', 'Chips'], ['Chips', 'Cheese', 'Cheese', 'Meat'], ['Chips', 'Meat', 'Soap', 'Cheese', 'Bread', 'Cola', 'Bread', 'Beer', 'Meat', 'Cola', 'Bread', 'Cola', 'Ketchup', 'Bread'], ['Chips', 'Cheese', 'Milk', 'Meat', 'Milk', 'Beer', 'Chocolate', 'Ketchup', 'Cola', 'Cheese', 'Beer'], ['Beer', 'Ketchup', 'Yoghurt', 'Ketchup', 'Chocolate', 'Bread', 'Beer', 'Ketchup', 'Chocolate', 'Cola', 'Chocolate', 'Ketchup', 'Cola', 'Meat', 'Chips', 'Soap', 'Meat'], ['Meat', 'Milk'], ['Cola', 'Beer', 'Yoghurt', 'Beer', 'Bread', 'Cola'], ['Chips', 'Meat', 'Cheese', 'Ketchup', 'Chips', 'Bread', 'Bread', 'Chips', 'Chips', 'Bread', 'Milk', 'Ketchup', 'Cola', 'Cola', 'Beer'], ['Beer', 'Bread', 'Cheese', 'Bread', 'Cola', 'Cheese', 'Cheese', 'Beer', 'Milk', 'Bread', 'Chocolate', 'Cheese', 'Beer', 'Bread', 'Beer', 'Cola', 'Yoghurt', 'Beer', 'Beer', 'Chips'], ['Bread', 'Chips', 'Bread', 'Cola', 'Chips', 'Chocolate', 'Cheese', 'Beer', 'Chips', 'Milk', 'Milk', 'Beer', 'Cola', 'Meat', 'Cola', 'Bread', 'Cola', 'Chocolate', 'Chocolate', 'Cola'], ['Soap', 'Yoghurt', 'Chips', 'Beer', 'Chips', 'Milk', 'Cheese', 'Meat', 'Beer', 'Bread', 'Ketchup', 'Bread', 'Bread', 'Cheese', 'Milk', 'Beer', 'Beer', 'Soap', 'Bread'], ['Cola', 'Bread', 'Cheese', 'Ketchup', 'Beer', 'Chips', 'Meat', 'Chocolate', 'Chips', 'Cola', 'Beer', 'Beer', 'Cola'], ['Ketchup', 'Beer', 'Chocolate', 'Bread', 'Yoghurt', 'Beer', 'Cheese'], ['Bread', 'Chocolate', 'Bread', 'Milk'], ['Meat', 'Yoghurt', 'Bread', 'Yoghurt', 'Cola', 'Ketchup'], ['Ketchup', 'Bread', 'Bread', 'Chocolate', 'Chocolate', 'Chocolate', 'Bread', 'Bread', 'Beer', 'Chocolate', 'Bread', 'Milk'], ['Bread', 'Cheese', 'Soap', 'Soap', 'Chips', 'Chips'], ['Ketchup', 'Chocolate', 'Chips', 'Milk', 'Soap', 'Soap', 'Ketchup', 'Bread', 'Ketchup', 'Cola', 'Cheese', 'Beer', 'Ketchup', 'Bread'], ['Bread', 'Milk', 'Beer', 'Yoghurt', 'Meat', 'Ketchup', 'Meat', 'Meat', 'Bread', 'Milk', 'Cheese', 'Beer', 'Yoghurt', 'Milk', 'Bread', 'Cola'], ['Chips', 'Cola', 'Milk', 'Chocolate', 'Beer', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Bread', 'Beer', 'Ketchup', 'Milk', 'Yoghurt', 'Ketchup', 'Cola', 'Ketchup', 'Chips', 'Meat'], ['Beer', 'Bread', 'Soap', 'Cheese', 'Meat', 'Soap'], ['Beer', 'Meat', 'Beer', 'Yoghurt', 'Soap', 'Chips', 'Meat', 'Cheese', 'Milk', 'Bread', 'Meat', 'Beer', 'Milk'], ['Chips', 'Meat', 'Bread'], ['Chocolate', 'Soap', 'Bread', 'Chips', 'Chips', 'Yoghurt', 'Chips', 'Cola', 'Cola', 'Cola', 'Beer', 'Milk', 'Milk', 'Bread', 'Bread', 'Meat'], ['Meat', 'Chocolate', 'Chips', 'Chips', 'Yoghurt', 'Yoghurt', 'Beer', 'Cola', 'Cheese', 'Milk', 'Beer'], ['Meat', 'Chocolate', 'Yoghurt', 'Cola', 'Cheese', 'Meat', 'Bread', 'Beer', 'Meat', 'Beer', 'Yoghurt', 'Cola', 'Bread']]
south = [['Cola', 'Meat', 'Cheese', 'Yoghurt', 'Beer', 'Milk', 'Milk', 'Meat', 'Cola', 'Cola', 'Cheese', 'Beer', 'Yoghurt', 'Beer', 'Bread', 'Bread', 'Milk', 'Cheese', 'Chocolate'], ['Soap', 'Milk', 'Cola'], ['Milk', 'Bread', 'Yoghurt', 'Meat', 'Meat'], ['Bread', 'Milk', 'Beer'], ['Beer'], ['Chocolate', 'Meat', 'Chocolate', 'Cola', 'Cola', 'Cola', 'Cola', 'Yoghurt', 'Bread', 'Meat', 'Soap', 'Soap', 'Milk', 'Milk', 'Cola'], ['Beer', 'Beer', 'Meat', 'Chips', 'Bread', 'Bread', 'Bread', 'Bread', 'Milk', 'Cola', 'Chocolate', 'Bread', 'Beer', 'Chips', 'Bread', 'Bread', 'Yoghurt'], ['Chips', 'Milk', 'Soap'], ['Meat', 'Beer', 'Milk', 'Chocolate', 'Bread', 'Yoghurt'], ['Chips', 'Meat', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Chocolate', 'Meat', 'Yoghurt', 'Milk'], ['Bread', 'Soap', 'Bread', 'Meat', 'Beer', 'Yoghurt', 'Milk', 'Cola', 'Bread', 'Ketchup'], ['Meat', 'Milk'], ['Meat', 'Beer', 'Yoghurt'], ['Cola', 'Bread', 'Cola', 'Chocolate', 'Chips', 'Meat', 'Cheese'], ['Milk', 'Milk', 'Cheese', 'Meat'], ['Chips', 'Yoghurt', 'Cheese', 'Soap', 'Ketchup', 'Cheese', 'Soap', 'Beer', 'Ketchup', 'Ketchup', 'Milk', 'Bread', 'Bread', 'Beer'], ['Meat'], ['Ketchup', 'Bread', 'Beer', 'Milk', 'Bread', 'Meat', 'Ketchup', 'Cheese'], ['Meat', 'Chips', 'Bread', 'Meat', 'Milk', 'Soap', 'Chocolate', 'Meat', 'Chocolate', 'Chocolate', 'Bread', 'Cheese', 'Soap', 'Cola', 'Yoghurt'], ['Cheese', 'Milk', 'Bread', 'Milk', 'Chips', 'Chips', 'Meat', 'Beer', 'Chocolate', 'Chocolate'], ['Ketchup', 'Beer', 'Cheese', 'Cola'], ['Chocolate', 'Cheese', 'Bread'], ['Milk', 'Yoghurt', 'Ketchup', 'Beer', 'Meat', 'Chips', 'Yoghurt', 'Meat', 'Bread', 'Chips'], ['Yoghurt', 'Milk', 'Ketchup', 'Yoghurt', 'Beer', 'Cheese', 'Bread', 'Bread', 'Ketchup', 'Bread', 'Bread', 'Yoghurt', 'Meat'], ['Soap', 'Meat', 'Bread', 'Beer', 'Milk'], ['Beer', 'Cola', 'Beer', 'Meat', 'Meat', 'Cheese', 'Meat', 'Chocolate', 'Bread', 'Ketchup', 'Milk', 'Soap'], ['Cheese', 'Chocolate', 'Milk', 'Chocolate', 'Cola', 'Bread', 'Chips', 'Cheese', 'Soap', 'Ketchup', 'Cheese', 'Chips', 'Cheese', 'Cola', 'Chocolate', 'Beer'], ['Bread', 'Bread', 'Cola', 'Ketchup', 'Cola', 'Bread', 'Meat', 'Yoghurt', 'Milk', 'Beer', 'Beer', 'Cheese', 'Meat', 'Bread', 'Cheese', 'Meat', 'Chocolate'], ['Chocolate', 'Soap', 'Chips', 'Beer', 'Bread', 'Yoghurt', 'Chips', 'Chocolate', 'Beer', 'Cheese', 'Cola', 'Milk', 'Chips', 'Milk', 'Ketchup', 'Cola', 'Meat', 'Beer', 'Cheese', 'Yoghurt'], ['Soap'], ['Meat', 'Beer', 'Milk', 'Bread', 'Beer', 'Cheese', 'Chocolate', 'Beer', 'Beer', 'Milk', 'Beer', 'Bread', 'Meat', 'Beer', 'Chocolate', 'Beer', 'Soap', 'Chips', 'Cola'], ['Cola', 'Beer', 'Meat', 'Chips', 'Soap', 'Cola', 'Bread', 'Cola', 'Bread', 'Chips', 'Ketchup', 'Ketchup', 'Beer', 'Ketchup', 'Cola', 'Milk', 'Cheese'], ['Cheese', 'Milk', 'Chips', 'Bread', 'Yoghurt', 'Soap', 'Beer', 'Chips', 'Ketchup', 'Chips', 'Beer', 'Yoghurt', 'Cola', 'Cheese', 'Chocolate', 'Beer'], ['Meat', 'Bread', 'Meat', 'Bread'], ['Cola', 'Beer', 'Yoghurt'], ['Beer', 'Bread', 'Beer', 'Meat', 'Bread', 'Milk', 'Soap', 'Milk', 'Chocolate', 'Meat', 'Meat', 'Meat', 'Chips', 'Chocolate', 'Meat'], ['Beer', 'Cola', 'Chocolate', 'Bread', 'Cheese', 'Cheese'], ['Milk', 'Chips', 'Cola', 'Milk', 'Bread', 'Bread', 'Beer', 'Milk', 'Cola', 'Chocolate', 'Chocolate', 'Meat', 'Cola', 'Cola', 'Beer', 'Cola', 'Chocolate', 'Bread', 'Bread', 'Cola'], ['Chocolate', 'Chocolate', 'Beer', 'Beer', 'Bread', 'Yoghurt', 'Meat', 'Cola', 'Yoghurt'], ['Ketchup', 'Cola', 'Ketchup', 'Yoghurt', 'Chips', 'Soap', 'Soap', 'Chocolate', 'Chocolate', 'Bread', 'Beer', 'Meat'], ['Bread', 'Meat', 'Soap', 'Cola', 'Bread', 'Cola', 'Yoghurt', 'Meat', 'Bread', 'Cola', 'Cola', 'Ketchup', 'Beer', 'Bread', 'Milk', 'Yoghurt', 'Meat'], ['Chocolate', 'Yoghurt', 'Bread'], ['Meat', 'Bread', 'Bread', 'Bread'], ['Beer', 'Milk', 'Cola', 'Ketchup', 'Cola', 'Cheese', 'Meat', 'Chocolate'], ['Soap', 'Beer', 'Chocolate', 'Chocolate', 'Cola', 'Cola', 'Yoghurt', 'Ketchup', 'Milk'], ['Meat', 'Yoghurt', 'Bread', 'Ketchup', 'Ketchup', 'Milk', 'Meat'], ['Ketchup', 'Soap', 'Chips', 'Ketchup', 'Bread', 'Chocolate', 'Milk', 'Bread', 'Bread', 'Ketchup', 'Cola', 'Meat', 'Milk', 'Bread', 'Cola'], ['Meat', 'Beer', 'Yoghurt', 'Chips', 'Beer', 'Meat', 'Cola', 'Beer', 'Meat', 'Ketchup', 'Milk', 'Cola', 'Yoghurt', 'Beer', 'Meat', 'Bread', 'Bread'], ['Meat', 'Soap', 'Cheese', 'Ketchup', 'Cola', 'Cola', 'Bread', 'Chips', 'Meat', 'Cola', 'Bread', 'Beer', 'Beer', 'Beer'], ['Meat', 'Yoghurt', 'Bread', 'Milk', 'Beer', 'Beer']]
# Пишите здесь команды, которые помогут
# найти ответы на вопросы
#a = Counter(north)
#ads = defaultdict(north)
rt = []
tt = []
uu = []
for i in range(len(north)):
    rt += north[i]
a = Counter(rt)
#print('счетчик а: ', a)
#print(sum(a.values()))

for i in range(len(center)):
    tt += center[i]
b = Counter(tt)
#print('счетчик b: ', b)
#print(sum(b.values()))

for i in range(len(south)):
    uu += south[i]
c = Counter(uu)
#print('счетчик c: ', c)
#print(sum(c.values()))

sum_all = a + b + c
#print('Сумма всех: ',sum_all)

sum_AB = a + b
k = c
#print(f'Сумма А и В: {sum_AB}')
k.subtract(sum_AB)
#print('C - sum_AB ', k)

sum_AС = a + c
y = b
y.subtract(sum_AС)
#print('B - sum_AC ', y)

sum_BС = b + c
u = a
u.subtract(sum_BС)
#print('A - sum_BС ', u)

# Есть ли такой товар, который в одном из магазинов покупали чаще, чем в двух 
# других вместе взятых? Если да, выберите магазин с настолько популярным товаром:
from collections import deque
from collections import defaultdict


tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

def task_manager(tasks):
    rr = deque()
    rt = deque()
    tasks = deque(tasks)
    dict_all = defaultdict(deque)
    for i in range(len(tasks)):
        #print(tasks[i][1])
        if tasks[i][1] == 'office' and tasks[i][2] == False:
         rr.append(tasks[i][0])
         #print(rr)
        elif tasks[i][1] == 'office' and tasks[i][2] == True:
         rr.appendleft(tasks[i][0])
        elif tasks[i][1] == 'voltage' and tasks[i][2] == False:
         rt.append(tasks[i][0])
        elif tasks[i][1] == 'voltage' and tasks[i][2] == True:
         rt.appendleft(tasks[i][0])
    
    dict_all['voltage'] = rt
    dict_all['office'] = rr

    return dict_all
    
print(task_manager(tasks))

import numpy as np
print(np.iinfo(np.int64))

b = np.uint8(-456)

n = -(2**64)/2 
hh = np.int64(n)
print('np.uint8(-456) = ', b)
print('инфа ', np.finfo(np.float32))


import numpy as np
arr = np.array([1,5,2,9,10], dtype=np.int8)
print('тип массива ',arr.dtype,'размерность массива: ', arr.itemsize)

zeros_3d = np.zeros((6,5,3), dtype=np.float32)
print(zeros_3d.shape)

# узнать щаг для создания массива -6 до 21 размером 60
step = np.linspace(-6, 21, 60, retstep=True, endpoint=False)
print(step)