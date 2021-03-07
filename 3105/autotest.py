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

    start_time = timeit.default_timer()
    qs(testarr, separ)
    time1 = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    sorted(testarr)
    time2 = timeit.default_timer() - start_time

    print(time1/time2)
    print(time1/sqrt(time2))