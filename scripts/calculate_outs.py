from collections import Counter
from itertools import product
from deuces import Card

def max_suited(hole, board):
    hand = hole + board
    suits = [Card.get_suit_int(card) for card in hand]
    suit_counts = Counter(suits)
    return max(suit_counts.values())

def flush_outs(hole, board):
    return 13 - max_suited(hole, board)

def max_connectors(hole, board):
    hand = hole + board
    ranks = [Card.get_rank_int(card) for card in hand]
    rank_counts = Counter(ranks)
    n = 0
    n_max = 0
    for key in [12] + rank_counts.keys():
        if rank_counts[key] > 0:
            n += 1
        else:
            n = 0
        n_max = max(n, n_max)
    return n_max


def straight_outs(hole, board):
    hand = hole + board



