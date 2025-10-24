from FlashiPy.core.card import Card
from FlashiPy.core.deck import Deck

# ALL_DECKS = []

# Russian_Deck = Deck("Russian Deck -_o")
# Japanese_Deck = Deck("Japanese Deck ^-^")

# ALL_DECKS.append(Russian_Deck)
# ALL_DECKS.append(Japanese_Deck)

# RU_CARD = Card(0, "мяу : Basic", "Meow \nExample: RU: Кот сказал 'мяу'. Romanized: Kot skazal 'myau'. EN: The cat said 'meow'.")
# JP_CARD = Card(0, "どうやって : N5", "How \nExample: JP: これはどうやって料理するのですか Romanized: Douyatte eki ni ikimasu ka? EN: How do I get to the station?")

# Russian_Deck.add_card(RU_CARD)
# Japanese_Deck.add_card(JP_CARD)

# print(Russian_Deck.list_cards())
# print(Japanese_Deck.list_cards())

# #Removing Cards

# Russian_Deck.remove_card(card_id=1)
# Japanese_Deck.remove_card(card_id=0)

# print(Russian_Deck.list_cards(), Japanese_Deck.list_cards())

# print("Printing all Decks", [d.name for d in ALL_DECKS])

with open("API", "r") as f:
    API_KEY = f.readline()
    print(API_KEY)


from FlashiPy.core.generator import Generator

gen = Generator(API_KEY)

print(gen.generate_card(language="Japanese", level="N1", topic="Rats"))

