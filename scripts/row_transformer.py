from deuces import Card, Evaluator

class RowTransformer:
    def __init__(self):
        self.evaluator = Evaluator()

    def prettify_row(self, row):
        cards = row.values[:7]
        cards = [Card.int_to_str(card) for card in cards]
        hand_evals = row.values[7:]
        hand_types = [self.evaluator.class_to_string(self.evaluator.get_rank_class(hand_eval)) for hand_eval in hand_evals]
        return cards + hand_types