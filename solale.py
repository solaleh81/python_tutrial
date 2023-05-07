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
    print(user)
    save_user(id=1, name="ali", age=32)
