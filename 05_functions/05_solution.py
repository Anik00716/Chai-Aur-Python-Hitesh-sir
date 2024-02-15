# Default Parameter Values
# Problem : Write a function that greet a user . If no name is provided , ot should greet  with a default name 

def greet(name = 'User'):
    return "Hello, " + name +" !"

print(greet("chai"))
print(greet())
