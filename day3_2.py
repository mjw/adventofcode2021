with open("input_day3") as f:
    data = [d[:-1] for d in f.readlines()]

def scrubber(data, depth=0):
    if len(data)==1:
        return data[0]

    ones = [s for s in data if s[depth]=="1"]
    zeros = [s for s in data if s[depth]=="0"]

    if len(ones)==len(zeros):
        return scrubber(zeros, depth+1)
    elif len(ones)>len(zeros):
        return scrubber(zeros, depth+1)
    else:
        return scrubber(ones, depth+1)

def oxygen(data, depth=0):
    if len(data)==1:
        return data[0]

    ones = [s for s in data if s[depth]=="1"]
    zeros = [s for s in data if s[depth]=="0"]

    if len(ones)==len(zeros):
        return oxygen(ones, depth+1)
    elif len(ones)>len(zeros):
        return oxygen(ones, depth+1)
    else:
        return oxygen(zeros, depth+1)

print("Oxygen generator %s" % oxygen(data), "CO2 scrubber %s" % scrubber(data))
print("Life support %d" % (int(oxygen(data),2) * int(scrubber(data),2)))
