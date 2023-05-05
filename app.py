x = 1
print(x)
print("neon")
student_count = 30.5
print(student_count)
is_published = True
print(is_published)
y = 100
print(y)

course = "python programming"
print(len(course))
print(course[9])
print(course[0:4])
print(course[:-3])
print("python programming")

# a variable for test

# escape sequnces
# \"
course = "python \" programming"
print(course)
# \'
course = 'python \' programming'
print(course)
# \\   back slash
course = "python \\ programming"
print(course)
# \n    enter
course = "python \n programming"
print(course)
course = """python
programming
"""
print(course)
# \t     tab
course = "python \t programming"
print(course)

# methods
course = "    python   programming        "
print(course.upper())
print(course.lower())
print(course.strip())
print(course.find("p"))

print(course.replace("p", "z"))


discount_code = "    256kl   "
print(discount_code.rstrip())
print(discount_code.lstrip())

# upprator
course = "python programming"
print("py" in course)
print("df" not in course)
