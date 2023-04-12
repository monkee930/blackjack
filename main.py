import random

cards = {
    'Ace': 11,
    'King': 10,
    'Queen': 10,
    'Jack': 10,
    'Ten': 10,
    'Nine': 9,
    'Eight': 8,
    'Seven': 7,
    'Six': 6,
    'Five': 5,
    'Four': 4,
    'Three': 3,
    'Two': 2
}

card_names = list(cards.keys())

class Deck:
    def __init__(self):
        self.cards = list(cards.keys()) * 4
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        self.cards.append(card)
        
    def __str__(self):
        return ', '.join(self.cards)

    def get_value(self):
      value = 0.0
      for card in self.cards:
          if card != 'Ace':
            value += cards[card]
      if 'Ace' in self.cards:
          if value + cards['Ace'] > 21:
            value += 1
          else:
            value += cards['Ace']
      return value

        
class Player:
    def __init__(self):
        self.hand = Hand()
        
    def hit(self, deck):
        self.hand.add_card(deck.deal_card())
        
    def is_bust(self):
        return self.hand.get_value() > 21
    
    def has_blackjack(self):
        return len(self.hand.cards) == 2 and self.hand.get_value() == 21
    
class Dealer:
    def __init__(self):
        self.hand = Hand()
        
    def hit(self, deck):
        self.hand.add_card(deck.deal_card())
        
    def is_bust(self):
        return self.hand.get_value() > 21
    
    def has_blackjack(self):
        return len(self.hand.cards) == 2 and self.hand.get_value() == 21
        
deck = Deck()
player = Player()
dealer = Dealer()

# Deal two cards to player and dealer
player.hit(deck)
player.hit(deck)
dealer.hit(deck)
print("Your hand:", player.hand)
print("dealer's's hand:", dealer.hand.cards, "as well as a secret card")

dealer.hit(deck)
# Player's turn
while True:
    action = input("Do you want to hit or stand? ")
    
    if action == 'hit':
        player.hit(deck)
        print("Your hand:", player.hand)
        
        if player.is_bust():
            print("You are almost as bad as Elio! Dealer wins.")
            break
    elif action == 'stand':
        break
        
# Dealer's turn
if not player.is_bust():
    print("Dealer's hand:", dealer.hand)
    
    while dealer.hand.get_value() < 17:
        dealer.hit(deck)
        print("Dealer hits:", dealer.hand)
        
        if dealer.is_bust():
            print("Dealer busts! You win.")
            break
            
    if not dealer.is_bust():
        if player.hand.get_value() > dealer.hand.get_value():
            print("You win!")
        elif player.hand.get_value() == dealer.hand.get_value():
            print("Push!")
        else:
            print("Dealer wins!")
