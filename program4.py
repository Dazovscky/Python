import math

t1=(155,146)
t2=(65,184)
R=6371

dist=math.sqrt((t2[0]-t1[0])**2 + (t2[1]-t1[1])**2)

L=dist*R

print(dist)
print(L)