import random
#testarr = [random.randint(0, 10) for item in range(10)]
#testarr = []
#print(testarr)

def tester(qs):
    testarr = [random.randint(0, random.randint(0,100)) for item in range(random.randint(0,100))]
    sortarr = qs(testarr)
    if(len(testarr)==0):
        assert sortarr == "no numbers"
    else:
        assert sorted(testarr) == sortarr 

def quicksort_fun(arr, start, end):
    if(len(arr)==0):
        return "no numbers"
    n = end
    if(start<end):
        sepindex = random.randint(start, end)
    else:
        sepindex = start
    sep = arr[sepindex]
    arr[sepindex] = arr[start]
    arr[start] = sep
    print(sep)
    s = 0
    i = start+1
    while(i<=n):
        if arr[i] >= sep:
            print(arr)
            while(s<=n-i): 
                if arr[n-s] <= sep:
                    buf = arr[i]
                    arr[i] = arr[n-s]
                    arr[n-s] = buf
                    print(arr)
                    s += 1
                    break
                s += 1
        i += 1
        #print("ok")
    arr[start] = arr[n-s]
    arr[n-s] = sep
    print(arr)
    if(n-s+1<n):
        quicksort_fun(arr, n-s+1, n)
    if(start<n-s-1):
        quicksort_fun(arr, start, n-s-1)
    return arr

def quicksort(array):
    return quicksort_fun(array, 0, len(array)-1)
    
tester(quicksort)
#print(quicksort(testarr))