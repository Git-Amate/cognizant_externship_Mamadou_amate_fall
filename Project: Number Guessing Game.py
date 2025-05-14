import random

number_to_guess = random.randint(1, 100)
#print(number_to_guess)
attempt_num = 1

while attempt_num <= 10:

    if attempt_num == 5 and number_to_guess%2 == 0:
        print(f"tips: the number to guess is even")
    elif attempt_num == 5 and number_to_guess%2 != 0:
        print(f"tips: the number to guess is odd")

    if attempt_num == 8:
        print(f"tips: the number to guess is between {number_to_guess - 30} and {number_to_guess + 30}")

    user_try = int(input("Guess the random number : "))
    if user_try == number_to_guess:
        print(f"Congratulations! You guessed it in {attempt_num} attempts !")
        break
    elif user_try > number_to_guess :
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

    if attempt_num == 10:
        print(f"Game over! Better luck next time!")



    attempt_num +=1
