a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

D=b**2-4*a*c
print("D="+str(D))
if D<0:
 print("Кор2ей нет")
elif D==0:
 x=-b/(2*a)
 print("x="+ str(x))
else:
 x1=(-b+D**0.5)/(2*a)
 x2=(-b-D**0.5)/(2*a)
 print("x1="+str(x1))
 print("x2="+str(x2))