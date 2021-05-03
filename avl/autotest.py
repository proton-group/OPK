def tester(avl):
    test = avl()
    #test small rotate _ left
    test.insert(10)
    test.insert(20)
    test.insert(6)
    test.insert(5)
    test.insert(4)
    assert test.root.left.value == 5 and test.root.left.left.value == 4 and test.root.left.right.value == 6
    assert test.height < 4
    test.clear()
    
    #test small rotate _ right
    test.insert(10)
    test.insert(20)
    test.insert(6)
    test.insert(7)
    test.insert(8)
    assert test.root.left.value == 7 and test.root.left.left.value == 6 and test.root.left.right.value == 8
    assert test.height < 4
    test.clear()
    
    #test big rotate _ right
    test.insert(10)
    test.insert(20)
    test.insert(6)
    test.insert(8)
    test.insert(7)
    assert test.root.left.value == 7 and test.root.left.right.value == 8 and test.root.left.left.value == 6
    
    #test big rotate _ left
    test.clear()
    test.insert(10)
    test.insert(20)
    test.insert(6)
    test.insert(7)
    test.insert(8)
    assert test.root.left.value == 7 and test.root.left.right.value == 8 and test.root.left.left.value == 6