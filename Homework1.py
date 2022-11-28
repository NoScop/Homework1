num = int(input('Введите число: '))
if num == 6 or num == 7:
    print('Да')
elif num > 0 and num < 6:
    print('Нет')
else:
    print('Введите цифру от 1 до 7')
    
 for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not(x or y or z) == (not x or not y or not z))
            print(x,y,z)
    
x = int(input('Введите координату x≠0: '))
y = int(input('Введите координату y≠0: '))
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
    
import math
x1 = int(input('Введите координату x точки А: '))
y1 = int(input('Введите координату y точки А: '))
x2 = int(input('Введите координату x точки В: '))
y2 = int(input('Введите координату y точки В: '))
print(round(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)),2))

