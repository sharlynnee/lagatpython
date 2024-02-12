# Inbuilt functions
number = max(79, 56, 90, 65, 43)
print(number)

x = min(30, 2, 54, 99)
print(x)

z = pow(2, 3)
print(z)


# User  defined functions
def name():
    print("Sharlene")


name()  # Calling a function


def student():
    name = ("Lagat")
    age = 18
    course = "MIT"
    print(name, age, course)


student()


def students(name, age, course):
    print(name, age, course)


students("Grace", "18", "MIT")
students("Lagat", 17, "Cybersecurity")
students("Collins", 32, "Cybersecurity")
students("Grace", "18", "MIT")
students("Lagat", 17, "Cybersecurity")
students("Collins", 32, "Cybersecurity")


def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)


employees("Sheila Lagat", 30, "female", "CEO", 500000)
employees("Ahrens Sitati", 28, "male", "Director", 420000)
employees("Eve Cheboi", 26, "female", "Accountant", 150000)
employees("Ian Debouy", 40, "male", "Manager", 450000)
employees("Val Koutes", 19, "female", "Secretary", 300000)
