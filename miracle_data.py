import re 


def numbers(data):
    day = set()
    day = re.findall(r'\d', data)
    #print('поиск регулярки', day)
    k = 0
    u = 0
    for i in range(4):
        k = k + int(day[i])
    #print('суммирование', k)
    day_midl = day[4:]
    for j in range(4):
        u = u + int(day_midl[j])
        print(u)
    #print('суммирование', u)
    return k, u

print(numbers('02061988'))