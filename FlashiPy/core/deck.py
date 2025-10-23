from .card import Card

class Deck:
    def __init__(self, name: str):
        self.name = name
        self.cards = []

    def add_card(self, card: Card):
        if not isinstance(card, Card):
            raise TypeError("Only cards can be added!")
        self.cards.append(card)

    def remove_card(self, card_id: int):
        self.cards = [c for c in self.cards if c.id != card_id]

    def list_cards(self):
        return "\n".join(str(c) for c in self.cards) if self.cards else "No cards yet."

    