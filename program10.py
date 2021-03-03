import math
D = 8
print("(D) Диаметр поперечного сечения = " + str(D))
A = 4
print("(A) Ширина квадратного бруса = " + str(A))
d = A * math.sqrt( 5 )
print("(d) Диагональ бруса = " + str(d))
if D >= d :
 print("Можно")
if D < d :
 print("Нельзя")