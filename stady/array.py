import numpy as np

vec = np.array([14,15,9,26,53,5,89])
print(vec <= 26)


vec = np.array([3, 4])
length = np.linalg.norm(vec)
print(length)

# сумма длин сонаправленных 
# векторов должна быть равной 
# длине суммы двух векторов.
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

aa = np.linalg.norm(a)
bb = np.linalg.norm(b)
cc = np.linalg.norm(c)

if aa + bb ==  np.linalg.norm(a + b): print('Сонаправлены: ', True)
else: print('Сонаправлены: ', False)
if aa + cc ==  np.linalg.norm(a + c): print('Сонаправлены: ', True)
else: print('Сонаправлены: ', False)
if bb + cc ==  np.linalg.norm(b + c): print('Сонаправлены: ', True)
else: print('Сонаправлены: ', False)

# Найдите пару векторов, расстояние 
# между которыми больше 100.
distance1 = np.linalg.norm(a - b)
distance2 = np.linalg.norm(b - c)
distance3 = np.linalg.norm(a - c)
if distance1 > 100: print('Расстояние больше 100: ', True)
else: print('Расстояние больше 100:', False)
if distance2 > 100: print('Расстояние больше 100:', True)
else: print('Расстояние больше 100:', False)
if distance3 > 100: print('Расстояние больше 100:', True)
else: print('Расстояние больше 100:', False)

# Найдите пару перпендикулярных векторов
# с помощью скалярного произведения
# (оно должно быть равно нулю).
if distance1 == 0: print('0: ', True)
else: print('0:', False)
if distance2 == 0: print('0: ', True)
else: print('0:', False)
if distance3 == 0: print('0: ', True)
else: print('0:', False)

choice = np.random.choice([2,4,6,8,10,12,14,16], size=4)
#print('choice ', choice)



def get_chess(a):
    
    zeros_3d = np.zeros((a, a))
    k = np.arange(0, a, 2)
    y = np.arange(1, a, 2)

    zeros_3d[::2,y] = 1
    zeros_3d[1::2,k] = 1
    return zeros_3d
print(get_chess(1))

#Задание 10.7 (Внешний источник)
def shuffle_seed(array):
    seed = np.random.randint(0, 2**32, size=1, dtype=np.int64)
    np.random.seed(seed)
    shuffled = np.random.permutation(array)
    return shuffled, seed
array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))

# ЗАДАНИЕ 10.8 
def min_max_dist(*vectors):
    dists = list()
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            dists.append(np.linalg.norm(vectors[i] - vectors[j]))
    return (min(dists), max(dists))


vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])
 
print(min_max_dist(vec1, vec2, vec3))


