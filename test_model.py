import pytest
from main import *

def test_givenDefaultFruit_FruitsAreCorrect():
    given = CMain()
    expected = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    answer = given.getInputs()
    assert expected == answer

def test_givenDefault_ScoreIsCorrect():
    given = CMain()
    expected = 5.142857142857143
    assert expected == given.getModelScore(given.getInputs())
