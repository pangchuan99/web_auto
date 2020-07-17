import pytest



@pytest.mark.parametrize("test_input,expected",
                         [
                             ("1+3", 4),
                             ("11+3", 14)
                         ])
def test_eval(test_input, expected):
    a = test_input
    print("\n",a)
    assert eval(a) == expected














# def test_eval_1():
#     a = "11+3"
#     assert eval(a) == 14