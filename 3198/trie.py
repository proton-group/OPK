# -*- coding: utf-8 -*-
class TrieNote:
    def __init__(self):
        self.ancestor = "no data"
        self.descendant = {}
        self.value = "no data"
        self.key = "no data"

class Trie:
    def __init__(self):
        self.notes = []
        self.cur = 0
        root = TrieNote()
        self.notes.append(root)
    
    def set(self, char, value):
        desInd = 0
        for i in range(len(char)):
            if char[i] in self.notes[desInd].descendant:
                desInd = self.notes[desInd].descendant[char[i]]
                if char[i] == char[len(char)-1]:
                    last_ind = desInd
                continue                
            
            note = TrieNote()
            self.notes.append(note)

            if i > 0:
                #self.notes[self.cur + 1].key = char[i]
                self.notes[self.cur + 1].ancestor = i
                self.notes[self.cur].descendant.update({char[i] : self.cur + 1})
                
            else:
                self.notes[0].descendant.update({char[i] : self.cur + 1})
                #self.notes[self.cur + 1].key = char[i]
            self.cur += 1
            last_ind = self.cur
        self.notes[last_ind].value = value
    
    def read(self, key):
        desInd = 0
        for i in range(len(key)):
            if key[i] in self.notes[desInd].descendant:
                desInd = self.notes[desInd].descendant[key[i]]
            else:
                return "no data"
        return self.notes[desInd].value

books = Trie()
books.set("hello", 5)
books.set("hells", 10)
books.set("Dostoevsky", 10)
print(books.notes)
print(books.read("hellos"))
print(books.read("Dostoevsky"))