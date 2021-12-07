with open("input_day1") as f:
    data = [int(x) for x in f.readlines()]

sums = []
b,c,*d = data

while d:
  a,b,c,*d = [b, c] + d
  sums.append(a + b + c)

print(sum([int(a < b) for (a, b) in zip(sums, sums[1:])]))

