from deuces import Card, Deck, Evaluator


def compute_win_prob(row, deck, evaluator):
    n_wins = 0
    n_hands = len(row)

    for _, hand in row.iterrows():
        # Prepare deck
        used_cards = hand[['hole1', 'hole2', 'flop1', 'flop2', 'flop3', 'turn', 'river']].astype(int).tolist()
        deck.shuffle()
        for card in used_cards:
            deck.cards.remove(card)

        # Board
        board = used_cards[2:]

        # Opponent evaluations
        opponent_scores = []
        for _ in range(hand['opponents']):
            opponent_hole = deck.draw(2)
            opponent_scores.append(evaluator.evaluate(opponent_hole, board))

        if hand['river_eval'] <= min(opponent_scores):
            n_wins += 1

    return n_wins / n_hands
