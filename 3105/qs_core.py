import random

def swap(arr, a, b):
    c = arr[a]
    arr[a] = arr[b]
    arr[b] = c

def partition(arr, sep, start, end):
    n = end
    s = 0
    i = start+1
    while(i<=n):
        if arr[i] >= sep:
            while(s<=n-i): 
                if arr[n-s] <= sep:
                    buf = arr[i]
                    arr[i] = arr[n-s]
                    arr[n-s] = buf
                    s += 1
                    break
                s += 1
        i += 1
    return arr, n-s

def sep_chooser(arr, start, end):
    if(start<end//3):
        ind1 = random.randint(start, end//3)
        num1 = arr[ind1]
        ind2 = random.randint(end//3, end//2)
        num2 = arr[ind2]
        ind3 = random.randint(end//2, end)
        num3 = arr[ind3]
    elif(start>=end):
        return start
    else:
        return random.randint(start, end)
    if(num1>=num2) and (num1>=num3):
        return ind1
    elif(num2>=num1) and (num2>=num3):
        return ind2
    else:
        return ind3