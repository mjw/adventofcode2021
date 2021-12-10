import numpy

with open("input_day5") as f:
    lines = f.readlines()

diagram = numpy.zeros((1000,1000),int)

for coords in lines:
    x1, y1 = map(int, coords.split()[0].split(','))
    x2, y2 = map(int, coords.split()[2].split(','))

    if y1==y2:
        diagram[y1, min(x1,x2):max(x1,x2)+1]+=1
    elif x1==x2:
        diagram[min(y1,y2):max(y1,y2)+1, x1]+=1

print(len(numpy.argwhere(diagram>1)))
