from src.math_operations import add, sub, mult, div


def test_add():
    assert add(2,3)     == 5
    assert add(-1,1)    == 0

def test_sub():
    assert sub(5,3)     == 2
    assert sub(1,-1)    == 2
    assert sub(10,4)    == 6
    assert sub(5,6)     == -1

def test_mult():
    assert mult(1,2)    == 2
    assert mult(2,2)    == 4
    assert mult(10,20)  == 200
    assert mult(100,13) == 1300


def test_div():
    assert div(1,2)    == 0.5
    assert div(2,2)    == 1
    assert div(10,20)  == 0.5
    assert div(100,10) == 10