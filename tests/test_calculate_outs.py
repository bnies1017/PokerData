import pytest
from scripts.calculate_outs import *

def test_max_suited():
    hole1 = [Card.new('Ah'), Card.new('Th')]
    board1 = [Card.new('Kh'), Card.new('3h'), Card.new('Jh')]
    assert max_suited(hole1, board1) == 5
    board2 = [Card.new('Ts'), Card.new('Ks'), Card.new('3s'), Card.new('Js')]
    assert max_suited(hole1, board2) == 4

def test_max_connectors():

