
import random
import timeit

testarr = sorted(random.sample(range(1, 100), 10))
arrover = sorted(random.sample(range(101, 200), 10))
#testarr = [2,3,4,5,6,7,8,9]

# def binary_search(arr, key):
#     index = (len(arr)-1)//2
#     base = index
#     if key == arr[0]:
#         return 0
#     while key != arr[0]:
#         if arr[(len(arr)-1)//2] == key:
#             break
#         elif arr[(len(arr)-1)//2] > key:
#             arr = arr[:(len(arr)-1)//2]
#             index = index - (len(arr)-1) // 2
#             print(arr)
#         elif arr[(len(arr)-1)//2] < key:
#             arr = arr[(len(arr)-1)//2:]
#             index = index + (len(arr)-1) // 2
#             print(arr)
#         if len(arr) == 0:
#             return "No numbers"
#         if (len(arr) == 1) and (arr[0] != key):
#             return "No numbers"
#     return index

def binary_search(arr, key, left, right):
    if(key > arr[right]) or (key < arr[left]):
        return "No numbers"
    sred = (left+right)//2
    if (left==right):
        return sred
    if arr[sred] == key:
        return sred
    if arr[sred] < key:
        return binary_search(arr, key, sred+1, right)
    if arr[sred] > key:
        return binary_search(arr, key, left, sred-1)

def test(arr, index):
    if len(arr) == 1:
        assert index == arr[0]
    elif len(arr) == 0:
        assert index == "No numbers"
    elif len(arr)%2 == 0:
        testindex = random.randint(0, len(testarr) - 1)
        assert (binary_search(testarr, testarr[testindex], 0, len(testarr)-1) == testindex) or (binary_search(testarr, testarr[testindex], 0, len(testarr)-1) == "No numbers")
        testindex = random.randint(0, len(testarr)-1)
        assert (binary_search(testarr, testarr[testindex], 0, len(testarr)-1) == testindex) or (binary_search(testarr, testarr[testindex], 0, len(testarr)-1) == "No numbers")
    for i in range(len(arr)-1):
        assert (binary_search(arr, arr[i], 0, len(arr)-1) == i)
        print("Индекс = {}, Число поиска = {}".format(binary_search(arr, arr[i], 0, len(arr)-1), arr[i]))
        print(arr)
        assert (binary_search(arr, arrover[i], 0, len(arr)-1) == "No numbers")
    return True

sarr = binary_search(testarr, testarr[2], 0, len(testarr)-1)
test(testarr, sarr)
