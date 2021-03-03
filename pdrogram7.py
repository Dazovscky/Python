import time
a=time.strftime('%H:%M:%S', time.gmtime(1235))
b=str(a)
c=b.replace(":", "/")
print(c)