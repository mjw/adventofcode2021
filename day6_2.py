import numpy

with open("input_day6") as f:
    lines = f.readlines()

fish_states = numpy.zeros(9,int)
for f in map(int, lines[0].split(',')):
    fish_states[f]+=1

for day in range(256):
    baby_fish = fish_states[0]
    fish_states = fish_states[1:]
    fish_states[6] += baby_fish
    fish_states = numpy.append(fish_states,baby_fish)
print(fish_states.sum())
