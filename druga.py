arr = [12, 5, 8, 21, 3, 16, 9, 14]

def vsota(arr):
    return sum(arr)
def povprecna(arr):
    return sum(arr) / len(arr)
def najvecji(arr):
    return max(arr)
def najmansi(arr):
    return min(arr)
def deljivost(st):
    return st % 2
def soda(arr):
    v = 0
    for i in range(len arr):
        if(deljivost(arr[i])):
            v += 1
    return v
def liha(arr):
    v = 0
    for i in range(len arr):
        if(not deljivost(arr[i])):
            v += 1
    return v
def velikost(arr):
    a = []
    for i in range(len(arr)):
        if(arr[i] > 10):
            a.append(arr[i])
    return a


print(velikost(arr))
