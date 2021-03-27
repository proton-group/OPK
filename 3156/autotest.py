def search_test(my_strstr):
    assert my_strstr("newworldsaveabobaeartheliphan", "aboba") == "Подстрока aboba найдена в строке в диапазоне от 13 символа до 17 символа"
    #тест с повторами
    assert my_strstr("abobaabobaabobaaboba", "aboba") == "Подстрока aboba найдена в строке в диапазоне от 1 символа до 5 символа"
    #тест с пробелом
    assert my_strstr("Hello World", "World") == "Подстрока World найдена в строке в диапазоне от 7 символа до 11 символа"
    #тест с русским
    assert my_strstr("привет", "ивет") == "Подстрока ивет найдена в строке в диапазоне от 3 символа до 6 символа"
    #тест с цифрами
    assert my_strstr("пр5и5вет2", "ивет") == "подстрока не найдена"
    assert my_strstr("пр5ивет2", "ивет") == "Подстрока ивет найдена в строке в диапазоне от 4 символа до 7 символа"



