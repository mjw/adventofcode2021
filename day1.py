with open("input_day1") as f:
    data = [int(x) for x in f.readlines()]

print sum([int(a<b) for (a,b) in zip(data, data[1:])])
