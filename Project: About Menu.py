import turtle
boucle = True


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


def draw_branch(branch_length):
    if branch_length > 5:
        turtle.forward(branch_length)

        turtle.right(20)
        draw_branch(branch_length - 15)

        turtle.left(40)
        draw_branch(branch_length - 15)

        turtle.right(20)
        turtle.backward(branch_length)


while boucle:
    print("Welcome to the Recursive Artistry Program! Choose an option: \n")
    choice = int(input("1 - Calculate Factorial \n"
          "2 - Find Fibonacci \n"
          "3 - Draw a Recursive Fractal \n"
          "4 - Exit \n"))

    if choice == 1:
        n = int(input("Enter a number to find its factorial:"))
        while n < 0:
            n = int(input("Enter a number to find its factorial. the number must be superior or egal to zero:"))
        print(f"the factorial of {n} is {factorial(n)} \n")

    if choice == 2:
        n = int(input("Enter the position of the Fibonacci number: "))
        while n < 0:
            n = int(input("Enter the position of the Fibonacci number the number must be superior or egal to zero:"))
        print(f"the {n}th Fibonacci number is {factorial(n)} \n")

    if choice == 3:
        turtle.speed("fastest")
        turtle.left(90)
        turtle.up()
        turtle.backward(100)
        turtle.down()
        turtle.color("green")

        draw_branch(100)
        turtle.done()


