print("Task 1 - Writing Functions")

def greet_user(name):
    return f"hello {name}, how you doing today"

def add_numbers(a,b):
    return f"la somme de {a} et de {b} est égale a {a+b}"

print(greet_user("amate"))
print(add_numbers(5,8)+"\n")

print("Task 2 - Using Default Parameters")

def describe_pet(pet_name,animal_type="dog"):
    return f"i have a {animal_type} his name is {pet_name}"

print(describe_pet("ziggy"))
print(describe_pet("milano","cat")+"\n")

print("Task 3 - Functions with Variable Arguments")

def make_sandwich(*ingrediants):
    return f"Making a sandwich with the following ingredients: {' '.join(f'- {ingredient}' for ingredient in ingrediants)}"

print(make_sandwich("ham", "cheese", "lettuce", "tomato")+"\n")

print("Task 4 - Understanding Recursion")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(factorial(10))
print(fibonacci(6))



