number = 100
while number > 0:
    print(number)
    number //= 2


command = ""
while command != "exit":
    command = input(">>>")
    print(command)


# creat my function
def greet(first_name):
    print(f"hi {first_name}")


greet("peyman")
