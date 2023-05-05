temprature = 35
if temprature > 30:
    print("its warm")
    print("drink water")
elif temprature > 20:
    print("its nice")
else:
    print("its cold")

message = "its warm" if temprature > 40 else "its cool"
print(message)

# ternary operator
age = 22

if age >= 18:
    print("Eligible")
else:
    print("not Eligible")

message = "Eligible" if age >= 18 else "not Eligible"
print(message)
print([1, 2, 3, 4])

# logical operators
# and
# or
# not
high_income = False
good_credit = False
student = False
if student:
    print("Eligible")
else:
    print("not Eligible")

    # short circuit
    if student and high_income and good_credit:
        print("Eligible")
    else:
        print("not Eligible")

# between condition
print("between condition")
if 18 <= age < 65:
    print("true")
else:
    print("false")
