import pytest
from deuces import Card
from scripts.classify_hole import *

def test_pair():
    hole1 = [Card.new('Ah'), Card.new('Ks')]
    assert pair(hole1) == False
    hole2 = [Card.new('Ah'), Card.new('As')]
    assert pair(hole2) == True

def test_suited():
    hole1 = [Card.new('Ah'), Card.new('Ks')]
    assert suited(hole1) == False
    hole2 = [Card.new('Ah'), Card.new('Kh')]
    assert suited(hole2) == True

def test_broadway():
    hole1 = [Card.new('Th'), Card.new('Ks')]
    assert broadway(hole1) == True
    hole2 = [Card.new('Th'), Card.new('9h')]
    assert broadway(hole2) == False

def test_connectors():
    hole1 = [Card.new('Ah'), Card.new('Ks')]
    assert connectors(hole1) == True
    hole2 = [Card.new('Ah'), Card.new('2h')]
    assert connectors(hole2) == True
    hole3 = [Card.new('8h'), Card.new('3h')]
    assert connectors(hole3) == False