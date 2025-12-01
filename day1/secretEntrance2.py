# Day 1: Secret Enterance Part 2

def rotate(rotation, currDial):
    direction = rotation[0]
    distance = int(rotation[1:])

    zeroCounter = 0

    if direction == "R":
        distanceToStart = (99 - currDial) + 1
        if distance < distanceToStart:
            currDial += distance
        else:
            distance -= distanceToStart
            currDial = 0
            zeroCounter += 1
            while distance > 99:
                distance -= 100
                zeroCounter += 1
            currDial += distance
        if currDial == 0 and distance != 0:
            zeroCounter += 1
        return (currDial, zeroCounter)

    elif direction == "L":
        if distance <= currDial:
            currDial -= distance
        else:
            distance -= currDial + 1
            if currDial != 0:
                zeroCounter += 1
            currDial = 99
            while distance > 99:
                distance -= 100
                zeroCounter += 1
            currDial -= distance
        if currDial == 0 and distance != 0:
            zeroCounter += 1
        return (currDial, zeroCounter)
    else:
        return (currDial, zeroCounter)

dial = 50
password = 0
with open("input") as puzzleInput:
    for rotation in puzzleInput:
        (dial, zeroClicks) = rotate(rotation, dial)
        password += zeroClicks

print(password)
