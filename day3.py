from collections import Counter
with open("input_day3") as f:
    data = f.readlines()

sums = Counter()

for d in data:
    for i, f in enumerate(list(d[:-1])):
        sums[str(i)] += int(f)

gamma = [(len(data)-a)<a and "1" or "0" for (_, a) in sums.items()]
epsilon = [(len(data)-a)>a and "1" or "0" for (_, a) in sums.items()]

gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)

print(gamma*epsilon)

