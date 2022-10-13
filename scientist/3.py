def exchange(usd = 0, rub = 0, rate = 0):
    if len(locals()) == 3:
        print('ValueError: Too many arguments')
    elif len(locals()) < 2:\
        print('ValueError: Not enough arguments')
    else:
        if usd != None and rub != None:rate = rub / usd
        elif usd != None and rate != None: rub = usd * rate
        elif rub != None and rate != None: usd = rub / rate
    return usd, rub, rate
try:
    print(exchange(rub=1000, rate=85))
except (ValueError, TypeError, ZeroDivisionError) as e:
    print(e)

#if arg < 2:
 #   raise ValueError("Not enough arguments")
#if len(locals()) == 3:
#raise ValueError("Too many arguments")