from src.calc import calc
import pytest

class TestCalc:
    def test_mistakes(self):
        with pytest.raises(ValueError):
            calc('++')
            calc('--')
            calc('')
            calc('$')
            calc('5++5')
            calc('5///3')
            calc('5**5')
            calc('5%%5')
            calc('5--5')
            calc('1+')
            calc('*1')
            calc('111')
            calc('111 111')
            calc('+')
    def test_numbers(self):
        assert calc('5+5')==10
        assert calc('5*5')==25
        assert calc('5-5')==0
        assert calc('5%5')==0
        assert calc('5//5')==1
        assert calc('5/5')==1
        assert calc('5+5/2')==7.5
        assert calc('7*7*7')==343
        assert calc('7*5-3')==32
        assert calc('   1000//   5  ')==200
        assert calc('100%5*20')==0
        assert calc('123%3')==0
