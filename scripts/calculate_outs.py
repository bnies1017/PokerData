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
    unique_ranks = list(set([Card.get_rank_int(card) for card in hand]))
    if 12 in unique_ranks:
        unique_ranks.insert(0,-1)
    n = 1
    n_max = 1
    for i in range(len(unique_ranks) - 1):
        if unique_ranks[i] == unique_ranks[i + 1]-1:
            n += 1
            n_max = max(n, n_max)
        else:
            n = 1
    return n_max


def straight_outs(hole, board):
    hand = hole + board
    unique_ranks = list(set([Card.get_rank_int(card) for card in hand]))
    if 12 in unique_ranks:
        unique_ranks.insert(0, -1)
    n = 1
    n_max = 1
    for i in range(len(unique_ranks) - 1):
        if unique_ranks[i] == unique_ranks[i + 1] - 1:
            n += 1
            n_max = max(n, n_max)
        else:
            n = 1



