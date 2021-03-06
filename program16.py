d = int ( input ("Введите диапазон: "))

print ("1")

print ("2")
for n in range (3, d):
        for a in range (2, n):
            if (n % a) == 0:
                break
            else:
                print (n)
                break
