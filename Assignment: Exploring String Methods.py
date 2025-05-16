print("Task 1 - String Slicing and Indexing")

s = "Python is amazing!"

print("Extracting the first 6 characters")
first_six_characters = s[0:7]
print(first_six_characters+"\n")

print("Extracting The word amazing")
amazing_word = s[10:17]
print(amazing_word+"\n")

print("The entire string in reverse order")
reverse_string = s[::-1]
print(reverse_string+"\n")

print("Task 2 - String Methods")

s = " hello, python world! "
print("demo of strip() = "+s.strip())
print("demo of capitalize() = "+s.strip().capitalize())
print("demo of replace() = "+s.replace("world","universe"))
print("demo of upper() = "+s.upper()+"\n")

print("Task 3 - Check for Palindromes")

x = input("put your word for checking: ")

if x[::-1] == x :
    print(f"your word '{x}' is a Palindromes!")
else:
    print(f"your word '{x}' is not a Palindromes!")
