import random
import timeit
from math import sqrt

def tester(qs, separ):
    testarr = []
    sortarr = qs(testarr, separ)
    assert sortarr == "no numbers"
    testarr = [1]
    sortarr = qs(testarr, separ)
    assert sortarr == [1]
    testarr = [random.randint(-100, 100) for item in range(random.randint(0,1000))]
    sortarr = qs(testarr, separ)
    assert sorted(testarr) == sortarr
    #print(sortarr)
    #10 elements
    for i in [10**deg for deg in range(2, 7)]:
        testarr = [random.randint(-100, 100) for item in range(random.randint(0, i))]
        start_time = timeit.default_timer()
        qs(testarr, separ)
        time1 = timeit.default_timer() - start_time
        #print(testarr)

        testarr = [random.randint(-100, 100) for item in range(random.randint(0, i))]
        start_time = timeit.default_timer()
        sorted(testarr)
        time2 = timeit.default_timer() - start_time
        print("qs time: {1:.2f} N={0}".format(i, time1))
        print("sorted time: {1:.2f} N={0}".format(i, time2))
        print("qs/sorted time: {1:.2f} N={0}\n".format(i, time1/time2))


def swap(arr, a, b):
#    c = arr[a]
#    arr[a] = arr[b]
#    arr[b] = c
    arr[b], arr[a] = arr[a], arr[b]

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

def find_median_idx(a, b, c):
    if a <= b and b <= c:
        return 1
    if b <= a and a <= c:
        return 0
    return 2

def sep_chooser(arr, start, end):
    if start < end//3:
        indices = [
            random.randint(start, end // 3),
            random.randint(end // 3, end // 2),
            random.randint(end // 2, end)
        ]
        values = [arr[item] for item in indices]
        return indices[find_median_idx(*values)]
        # ind1 =
        # num1 = arr[ind1]
        # ind2 =
        # num2 = arr[ind2]
        # ind3 =
        # num3 = arr[ind3]
        # if num2 <= num1 and num1 <= num3:
        #     # return ind1
        # # if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
        #     return ind1
        # elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
        #     return ind2
        # else:
        #     return ind3
    if start >= end:
        return start

    return random.randint(start, end)

import timeit
def quicksort_fun(arr, sep_chooser, start, end):
    if(len(arr)==0):
        return "no numbers"
    sep = sep_chooser(arr, start, end)
    swap(arr, sep, start)
    sep = arr[start]
    arr, sep = partition(arr, sep, start, end)
    swap(arr, start, sep)
    if(sep+1<end):
        quicksort_fun(arr, sep_chooser, sep+1, end)
    if(start<sep-1):
        quicksort_fun(arr, sep_chooser, start, sep-1)
    return arr

def quicksort(array, separ):
    return quicksort_fun(array, separ, 0, len(array)-1)

tester(quicksort, sep_chooser)
