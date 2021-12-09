import numpy
import sys

def check_lines(card):
    """Check for a win line by looking for a line of -1's"""
    for row in card:
        if (row==[-1,-1,-1,-1,-1]).all():
            return True

    for col in card.T:
        if (col==[-1,-1,-1,-1,-1]).all():
            return True

    return False

def mark_card(card, num):
    """Mark a card number by replacing all occurances with -1"""
    return numpy.where(card!=num,card,-1)

class Card():
    def __init__(self, data):
        self.card = data
        self.win = False
        self.num = -1

with open("input_day4") as f:
    called = [int(c) for c in f.readline().split(',')]

    data = [[int(n) for n in d.split()] for d in f.readlines() if d!="\n"]

    cards = []
    while data:
        a,b,c,d,e,*data = data
        cards.append(Card(numpy.array([a,b,c,d,e])))

lastwin = None

for num in called:
    for i in range(len(cards)):
        if (not cards[i].win):
            cards[i].card = mark_card(cards[i].card, num)
            if check_lines(cards[i].card):
                cards[i].win = True
                cards[i].num = num
                lastwin = cards[i]

print(lastwin.card)
print(lastwin.num)
print("Win!", numpy.where(lastwin.card!=-1,lastwin.card,0).sum()*lastwin.num)
