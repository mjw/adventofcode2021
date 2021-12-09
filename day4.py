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

with open("input_day4") as f:
    called = [int(c) for c in f.readline().split(',')]

    data = [[int(n) for n in d.split()] for d in f.readlines() if d!="\n"]

    cards = []
    while data:
        a,b,c,d,e,*data = data
        cards.append(numpy.array([a,b,c,d,e]))

for num in called:
    for i in range(len(cards)):
        cards[i] = mark_card(cards[i], num)
        if check_lines(cards[i]):
            print("Win!", numpy.where(cards[i]!=-1,cards[i],0).sum()*num)
            sys.exit()

print("Nowt won")
