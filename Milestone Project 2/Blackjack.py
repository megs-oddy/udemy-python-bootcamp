import random
from IPython.display import clear_output

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(rank,suit)
                self.deck.append(created_card)
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+ card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
    
    def __str__(self):
        hand_comp = ''  # start with an empty string
        for card in self.cards:
            hand_comp += '\n '+ card.__str__() # add each Card object's print string
        return 'Your hand has:' + hand_comp

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += (self.bet)*2
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('Please place a bet: '))
        except ValueError:
            print('Please enter a number!')
        
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed {chips.total}")
            elif chips.bet < 1:
                print('Sorry, your bet must be greater than 0.')
            else:
                break


def hit(deck,hand):
    
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    while True:
        HitStand = input("Hit or stand?: ")
        if HitStand == 'Hit' or HitStand == 'hit':
            hit(deck,hand)
            playing = True
            return playing
            
        elif HitStand == 'Stand' or HitStand == 'stand':
            print('Player stands. Dealer is playing.')
            playing = False
            return playing
        else:
            print('Please enter Hit or Stand')

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(chips):
    print('Player busts!')
    chips.lose_bet()
    
def player_wins(chips):
    print('Player wins!')
    playerchips.win_bet()   

def dealer_busts(chips):
    print('Dealer busts!')
    playerchips.win_bet()
    
def dealer_wins(chips):
    print('Dealer wins!')
    playerchips.lose_bet()
    
def push():
    print("It's a tie!")

if __name__ == "__main__": 
    playerchips = Chips()

    print('')
    print('Welcome to Black Jack!')

    gameon = True
    while gameon:
        
        # Print an opening statement

        
        # Create & shuffle the deck, deal two cards to each player 
        deck = Deck()
        deck.shuffle()
        
        player = Hand()
        dealer = Hand()
        
        hit(deck,player)
        hit(deck,dealer)
        hit(deck,player)
        hit(deck,dealer)
    

        print(f'\nYou have {playerchips.total} chips.')
        if playerchips.total <= 0:
            print('Sorry, you are out of chips!')
            print('Game Over')
            gameon = False
        
        else:
            # Prompt the Player for their bet
            take_bet(playerchips)

            # Show cards (but keep one dealer card hidden)
            show_some(player,dealer)

            playing = True
            while playing:  # recall this variable from our hit_or_stand function

                # Prompt for Player to Hit or Stand
                playing = hit_or_stand(deck, player)


                # Show cards (but keep one dealer card hidden)
                clear_output(True)
                show_some(player,dealer)

                # If player's hand exceeds 21, run player_busts() and break out of loop
                if player.value > 21:
                    player_busts(playerchips)
                    break


            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if player.value <= 21:
                while dealer.value < 17:
                    hit(deck,dealer)

                # Show all cards
                clear_output(True)
                show_all(player,dealer)

                # Run different winning scenarios
                if dealer.value > 21:
                    dealer_busts(playerchips)

                elif dealer.value > player.value:
                    dealer_wins(playerchips)

                elif dealer.value < player.value:
                    player_wins(playerchips)

                elif player.value == dealer.value:
                    push()

            # Inform Player of their chips total 
            print(f'You now have {playerchips.total} chips.')

            # Ask to play again

            while True:
                playagain = input('Would you like to play again? (Y or N): ')

                if playagain.lower() not in ['n','y']:
                    print('Please enter Y or N!')


                elif playagain.lower() == 'y':
                    clear_output(True)

                    break

                elif playagain.lower() == 'n':
                    print('Thank you for playing!')
                    gameon = False
                    break
            