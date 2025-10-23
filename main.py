from FlashiPy.core.card import Card
from FlashiPy.core.deck import Deck

ALL_DECKS = []

Russian_Deck = Deck("Russian Deck -_o")
Japanese_Deck = Deck("Japanese Deck ^-^")

ALL_DECKS.append(Russian_Deck)
ALL_DECKS.append(Japanese_Deck)

RU_CARD = Card(0, "мяу : Basic", "Meow \nExample: RU: Кот сказал 'мяу'. Romaji: Kot skazal 'myau'. EN: The cat said 'meow'.")
JP_CARD = Card(0, "どうやって : N5", "How \nExample: JP: これはどうやって料理するのですか Romaji: Douyatte eki ni ikimasu ka? EN: How do I get to the station?")

Russian_Deck.add_card(RU_CARD)
Japanese_Deck.add_card(JP_CARD)

print(Russian_Deck.list_cards())
print(Japanese_Deck.list_cards())

#Removing Cards

Russian_Deck.remove_card(card_id=1)
Japanese_Deck.remove_card(card_id=0)

print(Russian_Deck.list_cards(), Japanese_Deck.list_cards())

print("Printing all Decks", [d.name for d in ALL_DECKS])
