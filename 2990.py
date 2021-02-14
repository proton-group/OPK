from math import sqrt
numbers = int(input())
for i in range(numbers):
    count = 0
    for s in range(int(sqrt(i))+1):
        if s != 0:
            if(i % s == 0) and (s != 1) and (i != s):
                count += 1
    if count == 0:
        print(i)