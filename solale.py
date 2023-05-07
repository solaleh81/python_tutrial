def greet(first_name, last_name):
    print(f"hi {first_name} {last_name}")


greet("peyman", "amiri")


x = 200
while x > 0:
    print(x)
    x //= 10


def increment(number, by, another):
    return number + by - another


print(increment(number=2, by=1, another=20))

# multiplication table
for x in range(1, 10):
    for y in range(1, 10):
        print(x * y, end="\t\t")
    print("\n")


def save_user(**user):
    print(user["name"])


save_user(id=1, name="ali", age=32)


def greet(name):
    print(name)


greet("peyman")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(2, 3, 4))


letters = ["a", "b", "c"]

matrix = [[0, 1], [2, 3]]
print(letters[0])

zeros = [0] * 5
combined = letters + zeros
print(combined)


numbers = list(range(21))
print(numbers)

for number in range(20):
    print(0, end="\t")

    for x in range(1, 10):
        for y in range(1, 10):
            print(x * y, end="\t\t")
        print("\n")


letters = ["a", "b", "c", "d"]
print(letters[-2])
print(letters[-4])
print(letters[0])

numbers = list(range(20))
print(numbers[::2])
