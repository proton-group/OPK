import random
#testarr = [random.randint(0, 10) for item in range(10)]
#testarr = []
#print(testarr)
def sep_chooser(arr, start, end):
    if(start<end//3):
        ind1 = random.randint(start, end//3)
        num1 = arr[ind1]
        ind2 = random.randint(end//3, end//2)
        num2 = arr[ind2]
        ind3 = random.randint(end//2, end)
        num3 = arr[ind3]
    else:
        return random.randint(start, end)
    if(num1>=num2) and (num1>=num3):
        return ind1
    elif(num2>=num1) and (num2>=num3):
        return ind2
    else:
        return ind3

def tester(qs, separ):
    testarr = []
    sortarr = qs(testarr, separ)
    assert sortarr == "no numbers"
    testarr = [1]
    sortarr = qs(testarr, separ)
    assert sortarr == [1]
    testarr = [random.randint(-100, 100) for item in range(random.randint(0,100))]
    sortarr = qs(testarr, separ)
    assert sorted(testarr) == sortarr 
    print(sortarr)

def quicksort_fun(arr, separ, start, end):
    if(len(arr)==0):
        return "no numbers"
    n = end
    if(start<end):
        sepindex = separ(arr, start, end)
    else:
        sepindex = start
    sep = arr[sepindex]
    arr[sepindex] = arr[start]
    arr[start] = sep
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
        #print("ok")
    arr[start] = arr[n-s]
    arr[n-s] = sep
    if(n-s+1<n):
        quicksort_fun(arr, separ, n-s+1, n)
    if(start<n-s-1):
        quicksort_fun(arr, separ, start, n-s-1)
    return arr

def quicksort(array, separ):
    return quicksort_fun(array, separ, 0, len(array)-1)

tester(quicksort, sep_chooser)