# Day 1: Secret Enterance

def rotate(rotation, currDial):
    direction = rotation[0]
    distance = int(rotation[1:])

    dialVals = [i for i in range(0, 100)]

    if direction == "R":
        distanceToStart = (99 - currDial) + 1
        if distance < distanceToStart:
            currDial += distance
        else:
            distance -= distanceToStart
            currDial = 0
            while distance > 99:
                distance -= 100
            currDial += distance
        return currDial

    elif direction == "L":
        if distance <= currDial:
            currDial -= distance
        else:
            distance -= currDial + 1
            currDial = 99
            while distance > 99:
                distance -= 100
            currDial -= distance
        return currDial
    else:
        return currDial

dial = 50
password = 0
with open("input") as puzzleInput:
    for rotation in puzzleInput:
        dial = rotate(rotation, dial)
        print(dial)
        if dial == 0:
            password += 1

print(password)
