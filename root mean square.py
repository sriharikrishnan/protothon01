import math
def rmsvalue(arr,n):
    square=0
    mean=0.0
    root=0.0
    for i in range(0,n):
        square += (float(arr[i])**2)
    mean = square / (float(n))
    root = math.sqrt(mean)
    return root
arr = input().split(",") 
n = len(arr) 
print(rmsvalue(arr, n)) 
  
