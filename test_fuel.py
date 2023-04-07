from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(70) == "70%"
    assert gauge(100) == "F"