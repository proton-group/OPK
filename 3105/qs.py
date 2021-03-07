from qs_core import swap, partition, sep_chooser
from autotest import tester
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
