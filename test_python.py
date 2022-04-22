'''
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
Чем больше тестов на каждую функцию - тем лучше
'''
import math

def test_filter():
    name = ['Kate', 'Max', 'Leo', 'Poll']
    digit = [1, 2, 1, 3, 2, 4]
    assert type(filter(lambda x: 'a' in x, name)) == filter
    assert list(filter(lambda x: 'a' in x, name)) == ['Kate', 'Max']
    assert tuple(filter(lambda x: x == 2, digit)) == (2, 2)

def test_map():
    digit_str = ['1', '2', '3', '4']
    assert type(map(int, digit_str)) == map
    assert list(map(int, digit_str)) == [1, 2, 3, 4]
    assert tuple(map(lambda x: x * 2, digit_str)) == ('11', '22', '33', '44')
    assert tuple(map(lambda x: int(x) * 2, digit_str)) == (2, 4, 6, 8)

def test_sorted():
    s = 'hello'
    d = [2, 3, 1, 4]
    name = ['Kate', 'Max', 'Leo', 'Poll']
    assert type(sorted(s)) == list
    assert sorted(s) == ['e', 'h', 'l', 'l', 'o']
    assert sorted(s, reverse=True) == ['o', 'l', 'l', 'h', 'e']
    assert sorted(d) == [1, 2, 3, 4]
    assert sorted(d, reverse=True) == [4, 3, 2, 1]
    assert sorted(name, key=len) == ['Max', 'Leo', 'Kate', 'Poll']
    assert sorted(name, key=len, reverse=True) == ['Kate', 'Poll', 'Max', 'Leo']

def test_pi():
    assert math.pi == 3.141592653589793
    assert type(math.pi) == float
    assert math.pi > 0

def test_sqrt():
    assert math.sqrt(4) == 2
    assert type(math.sqrt(25)) == float

def test_pow():
    assert math.pow(2, 2) == 4
    assert math.pow(2, 3) == 8
    assert math.pow(2, 4) == 16
    assert type(math.pow(2, 2)) == float

def test_hypot():
    assert type(math.hypot(4, 3)) == float
    assert math.hypot(4, 3) == 5
    assert math.hypot(4, 3) == math.sqrt(4 * 4 + 3 * 3)

