import random
N=random.randint (0, 5)
arr = [random.randint (0, 80) for i in range(N)]
print(arr)
for i in range(0,N,3):
    arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)