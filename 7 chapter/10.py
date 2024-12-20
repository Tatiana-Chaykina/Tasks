def find_quirky_numbers(digit_count):
    a=[]
    for i in range(int ('1'+'0'*digit_count)):
        s=i
        i=str(i)
        while len(i)<digit_count:
            i='0'+i
        s1=int(i[:digit_count//2])
        s2 = int(i[(digit_count // 2):])
        if s1**2+2*s1*s2+s2**2==s:
            a.append(i)
    print(a)
    return a

# Тесты
def test_find_quirky_numbers():
    # Тест 1
    digit_count = 2
    expected_output = ['00', '01', '81']
    assert find_quirky_numbers(digit_count) == expected_output

    # Тест 2
    digit_count = 4
    expected_output = ['0000', '0001', '0004', '0009', '0016', '0025',
                       '0040', '0081', '0096', '0160', '0250', '0400',
                       '0640', '0810', '1000', '1024', '1600', '2025',
                       '2500', '3025', '3600', '4000', '6400', '8100',
                       '9600']
    assert find_quirky_numbers(digit_count) == expected_output

    # Тест 3
    digit_count = 6
    expected_output = []  # Не ожидается никаких "причудливых" чисел
    assert find_quirky_numbers(digit_count) == expected_output

    # Тест 4
    digit_count = 8
    expected_output = []  # Не ожидается никаких "причудливых" чисел
    assert find_quirky_numbers(digit_count) == expected_output

    print("OK!")


# Запустите тесты
test_find_quirky_numbers()