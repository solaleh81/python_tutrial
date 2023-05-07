# after for, we have iterable object
for number in range(4):
    print(number)
for number in range(4):
    print("message")

    for number in range(5):
        print((number+1) * ".")

    for number in range(1, 10, 3):
        print(number)

successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempet 3 times and failed.")

    for x in range(4):
        for y in range(3):
            print(f"({x},{y})")
