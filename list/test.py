def tester(slist):
    new = slist()
    new.append(1)
    new.append(2)
    new.prepend(0)
    new.append(3)
    for i in range(4):
        assert new.get(i) == i
    new.append_from_key(2, 2021) # вставка между
    assert new.get(2) == 2021
    assert new.length() == 5 # 0 1 2021 2 3
    connect = slist()
    connect.append(5)
    connect.append(6)
    new.concat(connect)
    assert new.length() == 7 and new.get(5) == 5 and new.get(6) == 6
    new.remove(2)
    assert new.get(2) == 2
    assert new.length() == 6
    test = slist()
    test.base = new.copy()
    assert test.get(2) == 2
    assert test.length() == 6