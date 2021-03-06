M = int( input ("Введите число M: "))

a = int( input ("Введите диапазон a: "))

b = int( input ("Введите диапазон b: "))

if a <= 0 and b <=0:
    print ("Ошибка! a и b должны быть > 0!")
elif b<= a:
    print ("Неверный диапазон! b должно быть больше a!")
else:
    print ("Результат:")
    for a in range (a-1, b):
         a += 1
         print (M, "x", a, "=", M * a)