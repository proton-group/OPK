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