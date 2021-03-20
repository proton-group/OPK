import autotest
#hash должен вычисляться из предыдущего
#надо бы еще кнут Мориса-Прата сделать

def hash_single(char):
    hash_fun = 0
    deg = 1
    mod = 99945668494
    for i in char: # n
        hash_fun += ord(i)*deg
        deg *= 256
    return (hash_fun % mod, hash_fun)

def rehash(char, first, pasthash, hasher):
    mod = 99945668494
    futurehash = (pasthash[1] - ord(first) + ord(char[len(char)-1])*256**(len(char)))//256
    #print("символ", ord(char[len(char)-1]))
    return (futurehash % mod, futurehash)

def my_strstr(haystack, needle):
    needle_hash = hash_single(needle)
    #print(needle_hash)
    for i in range(len(haystack)-len(needle)+1):
        if i == 0:
            haystack_hash = hash_single(haystack[i:len(needle)+i])
            #print("хастик", haystack[i:len(needle)+i])
        else:
            haystack_hash = rehash(haystack[i:len(needle)+i], haystack[i-1], haystack_hash, hash_single)
        #print(haystack_hash)
        if needle_hash[0] == haystack_hash[0]:
            count = 0
            for s in range(len(needle)):
                count += 1 if (haystack[i+s]==needle[s]) else 0
                #print(count)
            if count == len(needle):
                return "Подстрока {0} найдена в строке в диапазоне от {1} символа до {2} символа".format(needle, i+1, len(needle)+i)
            return "подстрока не найдена"  
        #print(compar)
    return "подстрока не найдена"
    
autotest.search_test(my_strstr)
