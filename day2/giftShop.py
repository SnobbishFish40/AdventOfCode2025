def findNextEvenDigits(value):
    nextEvenLength = 10**(len(value))
    value = str(nextEvenLength)
    return value

input = "input"
with open(input, "r") as file:
    ranges = file.read().strip()
    rangesList = ranges.split(",")

    sum = 0
    for range in rangesList:
        bounds = range.split("-")
        lower = bounds[0]
        upper = bounds[1]

        print("lower: ", lower)
        print("upper: ", upper)

        if len(lower) % 2 != 0:
            lower = findNextEvenDigits(lower)
            if int(lower) > int(upper):
                continue


        repeat = lower[:len(lower)//2]
        num = int(repeat * 2)

        while num <= int(upper):

            if len(str(num)) % 2 != 0:
                num = int(findNextEvenDigits(num))
                continue

            if num >= int(lower):
                sum += num
                print("Found: ", num)

            repeat = str(int(repeat) + 1)
            num = int(repeat * 2)

print(sum)

