#делаем таблицу из координат и записываем в нее буллианы, во второй таблице начения
#бинарный поиск
#disjoenset - unionfine
# list dict set map tuple
#реализовать словарь, чтобы не вывывать исключения
#использовать hash
from search import my_strstr
names = {"hello":2}
class trie:
    def __init__(self):
        self.tree = [[]]
        self.name = {}

    def set(self, key, data):
        for i in range(len(key)):
            if i > 0:
                if key[i] in self.name:
                        if self.three[self.name[key[i]]][self.name[key[i-1]]] == True:
                            
                else:
                    self.name.update({key[i] : len(self.tree)-1+i})
                    self.tree.append([])
                    self.tree[len(self.tree)-1].append(True)
                    self.tree[len(self.tree[len(self.tree)-1])].append(True)
