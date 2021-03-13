#hash должен вычисляться из предыдущего
#кнут морис прата
def hash_single(needle):
    hash_fun = 0
    count = 0
    deg = 1
    mod = 99945668494
    for i in needle: # n
        hash_fun += ord(i)*deg
        deg *= 256
    return hash_fun

def rehash(char_list, pasthash, hasher):
    futurehash = (pasthash - hasher(char_list[0]) + hasher(char_list[len(char_list)-1])*256**(len(char_list)-1))//256
    return futurehash

def my_strstr(haystack, needle):
    needle_hash = hash_single(needle)
    print(needle_hash)
    haystack_list = list(haystack)
    for i in range(len(haystack)-len(needle)):
        if i == 0:
            haystack_hash = hash_single([haystack_list[num] for num in range(i, len(needle)+i)])
        else:
            haystack_hash = rehash([haystack_list[num] for num in range(i, len(needle)+i)], haystack_hash, hash_single)
            print(haystack_hash)
        compar = True if needle_hash == haystack_hash else False
        print(compar)

my_strstr("oaegsghellohehh", "hello")
