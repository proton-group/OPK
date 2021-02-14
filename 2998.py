k_num = int(input())
a, b = 0, 1
for i in range(k_num):
    a, b = b, a+b
print(a)