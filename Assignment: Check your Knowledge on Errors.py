print("Task 1 - Understanding Python Exceptions")

try:
    user_input = int(input("put a number : "))
    result = 100 / user_input
    print(f"100 divided by {user_input} is {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid numeric value.")

print("Task 2 - Types of Exceptions")

# 1. IndexError
try:
    my_list = [10, 20, 30]
    # Trying to access index 5, which doesn't exist (only 0 to 2 are valid)
    print(my_list[5])
except IndexError:
    print("IndexError: Tried to access an index that doesn't exist in the list.")

# 2. KeyError
try:
    my_dict = {"name": "Alice", "age": 30}
    # Trying to access the key 'email' which is not in the dictionary
    print(my_dict["email"])
except KeyError:
    print("KeyError: Tried to access a key that doesn't exist in the dictionary.")


print("Task 2 - Types of Exceptions")

# 3. TypeError
try:
    # Trying to add a string and an integer
    result = "Age: " + 25
except TypeError:
    print("TypeError: Cannot add a string and an integer directly.")


print("Task 3 - Using try...except...else...finally")


try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numeric values.")
else:
    print(f"The result of dividing {num1} by {num2} is {result}")

finally:
    print("Program has finished executing.")


