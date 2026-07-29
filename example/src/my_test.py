from my import add, subtract

def test_add():
    assert add(1, 1) == 2, "Expected 1 + 1 to equal 2"

def test_subtract():
    assert subtract(3, 1) == 2, "Expected 3 - 1 to equal 2"
