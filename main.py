# "Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."

sumnum = 0

with open("numbers", "r") as f:
    for line in f:
        sumnum += int(line.rstrip())

print(sumnum)
print(str(sumnum)[0:10])