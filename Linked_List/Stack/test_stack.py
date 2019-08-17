from stack import st1
import pytest

def test_pop():
    assert st1.pop() == 10

@pytest.mark.great
def test_top():
    assert st1.Top() == 10

def test_pop1():
    assert st1.pop() == 9

def test_pop2():
    assert st1.pop() == 8

def test_pop3():
    assert st1.pop() == 7

def test_pop4():
    assert st1.pop() == 6

def test_pop5():
    assert st1.pop() == 5

def test_pop6():
    assert st1.pop() == 4

def test_pop7():
    assert st1.pop() == 3

def test_pop8():
    assert st1.pop() == 2

def test_pop9():
    assert st1.pop() == 1

def test_pop10():
    assert st1.pop() == 'Overflow!!!'