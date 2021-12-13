import numpy

with open("input_day7") as f:
    lines = f.readlines()

crabs = numpy.array(list(map(int, lines[0].split(','))))

print(min([numpy.where(crabs<i, i-crabs, crabs-i).sum() for i in range(crabs.min(), crabs.max()+1)]))
#                                                       for every possible alignment
#                                                 sum the total of
#          every fuel cost for movement to that position
#     and print the miniumum fuel cost
