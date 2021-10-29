from random import choice
from random import randint

class die_face():
    # This class is used to define the properties linked to each outcome on the dice.
    def __init__(self, num, colour, parity):
        self.num = num
        self.colour = colour
        self.parity = parity

# Determine the properties linked to each outcome on the dice.
zero = die_face(0, 'none', 'none')
one = die_face(1, 'blue', 'odd')
two = die_face(2, 'blue', 'even')
three = die_face(3, 'blue', 'odd')
four = die_face(4, 'green', 'even')
five = die_face(5, 'green', 'odd')
six = die_face(6, 'green', 'even')

options = [zero, one, two, three, four, five, six,]


class bet():
    # Define the bets
    def __init__(self, bet_type, odds):
        self.bet_type = bet_type
        self.odds = odds

num_bet = bet('num', 5)
colour_bet = bet('colour', 2)
parity_bet = bet('parity', 2)


class broker():
    # Define the properties of the broker.
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        result = 'Name:       ' + self.name + '\n'
        result += 'Balance:         ' + str(self.balance)
        return result

    def modify_balance(self, amount):
        self.balance += amount

main_broker = broker('Main',1e3)


def random_strategy():
    # Bet a random amount on a random game with a random guess.
    guess = 'empty'
    game_mode= choice([num_bet, colour_bet, parity_bet])
    if game_mode == num_bet:
        guess = randint(0,6)
    elif game_mode == colour_bet:
        guess = choice(['blue','green'])
    elif game_mode == parity_bet:
        guess = choice(['even','odd'])
    value = randint(1,10)
    return game_mode , value, guess


class player():
    # This class defines each player
        def __init__(self, name, strategy, bank_roll):
            self.name = name
            self.strategy = strategy
            self.bank_roll = bank_roll

        def modify_balance(self, amount):
            self.bank_roll += amount


        def __str__(self):
            result = 'Name:         ' + self.name + '\n'
            result += 'Bank Roll:       ' + str(self.bank_roll) + '\n'
            return result

        def play(self):
            return self.strategy()


# Add the players
Will = player("Will",random_strategy,100)


def dealer(type, bet_value, guess):
    #Roll the dice
    correct = choice(options)
    #Return amount based on Win or Lose
    if type == num_bet.bet_type:
        if correct.num == guess:
            return num_bet.odds * bet_value - bet_value
        else:
            return -bet_value

    if type == colour_bet.bet_type:
        if correct.colour == guess:
            return colour_bet.odds * bet_value - bet_value
        else:
            return -bet_value

    if type == parity_bet.bet_type:
        if correct.parity == guess:
            return parity_bet.odds * bet_value - bet_value
        else:
            return -bet_value

def main_play(player):
    # Collect the bets from the players
    bets = player.play()
    # Roll and return bets
    amount = dealer(bets[0].bet_type, bets[1], bets[2])
    # Distribute the money
    main_broker.modify_balance(amount*-1)
    player.modify_balance(amount)
