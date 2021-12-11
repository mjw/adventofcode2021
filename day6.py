import numpy

with open("input_day6") as f:
    lines = f.readlines()

fish = numpy.array(list(map(int, lines[0].split(','))))

for day in range(80):
    # decrement fish
    fish = fish-1

    # create new fish for every potential 6 (fish at -1)
    # happens when -1 before reset so we dont create fish
    # for new fish counting from 8
    fish = numpy.append(fish,numpy.full(len(numpy.argwhere(fish==-1)),8))

    # "reset" fish (-1 is reset)
    fish = numpy.where(fish>-1, fish, 6)

print(len(fish))
