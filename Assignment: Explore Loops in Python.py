print("Task 1 - Counting Down with Loops")

i = int(input("Enter the starting number:"))
print(i)
while i != 1:
    i -= 1
    print(i)
print("Blast off! \n")

print("Task 2 - Multiplication Table with for Loops")

j = int(input("Enter the starting number:"))
for i in range (0,11):
    print(f"{j} x {i} == {i*j} \n")

print("Task 3 - Find the Factorial")

x = int(input("Enter the starting number:"))
facto = x
for y in range(x-1,0,-1):
    facto = facto * y

print(f"The factorial of {x} is {facto}")


