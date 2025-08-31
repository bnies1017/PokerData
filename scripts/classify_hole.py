from deuces import Card, Evaluator
from skimage.transform import hough_ellipse


def pair(hole):
    hole1, hole2 = hole
    return Card.get_rank_int(hole1) == Card.get_rank_int(hole2)

def suited(hole):
    hole1, hole2 = hole
    return Card.get_suit_int(hole1) == Card.get_suit_int(hole2)

def broadway(hole):
    hole1, hole2 = hole
    return Card.get_rank_int(hole1) >= 8 and Card.get_rank_int(hole2) >= 8

def connectors(hole):
    hole1, hole2 = hole
    return abs(Card.get_rank_int(hole1) - Card.get_rank_int(hole2)) % 11 == 1

def ace(hole):
    hole1, hole2 = hole
    return Card.get_rank_int(hole1) == 12 or Card.get_rank_int(hole2) == 12

def two_seven(hole):
    hole1, hole2 = hole
    return ((Card.get_rank_int(hole1) == 0 and Card.get_rank_int(hole2) == 5) or
            (Card.get_rank_int(hole1) == 5 and Card.get_rank_int(hole2) == 0))

