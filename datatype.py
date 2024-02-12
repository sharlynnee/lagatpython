# Data Types
number = 45  # int
bun = 56.78  # float
greeting = "Hello there"  # str
isPythonInteresting = True  # bool

# variable storing multiple values
languages = ["python", "php", "java"]  # List
fruits = ("apple", "banana", "pineapple")  # Tackle
countries = {"Kenya", "China", "USA"}  # set
# Dictionary
details = {
    "firstname": "Grace",
    "age": 17,
    "course": "MIT"

}
print(details["age"])
print(details["course"])
print(number)
print(greeting)
print(countries)
print(isPythonInteresting)
print(details)

# Determining the data type
print(type(details))
print(type(countries))

# Type casting - Converting one datatype to another
print(int(number))
print(float(number))
