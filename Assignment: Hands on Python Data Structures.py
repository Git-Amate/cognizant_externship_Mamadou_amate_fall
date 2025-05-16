print("Task 1 - Working with Lists")

fruit_list = ["banana","orange","cherry","kaki","papaya","date","apple"]
print("this in the original list "+ fruit_list.__str__())
fruit_list.append("ananas")
print("this is the list adding one new fruit 'ananas' : " + fruit_list.__str__())
fruit_list.remove("orange")
print("this is the list removing one fruit 'orange' : " + fruit_list.__str__())
reverse_fruit_list = fruit_list[::-1]
print("this is the list reversed : " + reverse_fruit_list.__str__())

print("Task 2 - Exploring Dictionaries")

my_dictionary = {'name': 'Amate', 'age': '24', 'city': 'Gatineau', 'country': 'Canada'}
my_dictionary.update({'factorite_color':'blue'})
print("add new key-value pair to the dictionary for 'favorite color' : "+ my_dictionary.__str__() )
my_dictionary.update({'city':'montreal'})
print("Update the 'city' key with a new value. : "+ my_dictionary.__str__() )
for key,value in my_dictionary.items():
    print(f"the key is '{key}' and the value is '{value}'")

print("Task 3 - Using Tuples")

my_tuple = ("Teen Beach","thriller","l'os de mor lam")
#my_tuple[1] = 'wonderful life'
print("let's try to change the song 'thriller' by 'wonderful life' oups tuple are immutable")
print(f"the lengh of the tuple is {len(my_tuple)}")


