# Strings

# String literals are create by either using single or double quotes
# "This is a string."
# 'This is a string.'

# These strings have the same value

# to use them, we assign them to a variable 

# Why doesn't Python only use double or single quotes?

#  - A title is in your text 
book = 'The name of the book is "How The West Was Won".'
print (book)

#  - you have an apostrophe within
# response = "Let's go to the garden area."
# print (response)

# # What happens if you attempt to use one or the other?
# book = 'The name of the book is 'How The West Was Won'.'  # <- "Statements must be separated by newlines or semicolons"
# print(book)

# text = "Hello,\nWorld!"
# print(text)

# book = "The name of the book is \"How The West Was Won\"." # <- Legal, but why?
# print(book)
#book1 = 'The name of the book is '; book2 = '"How The West Was Won"'; book3 = '.'; print(book1 + book2 + book3)

# # Multi-line strings or doc strings, we use triple quotes or double quotes. Allowing strings to span multiple lines.

# very_long_string = "What if you have a very long string that spans the entire page? What happens? What if you have a very long string that spans the entire page? What happens?What if you have a very long string that spans the entire page? What happens?What if you have a very long string that spans the entire page? What happens?What if you have a very long string that spans the entire page? What happens?What if you have a very long string that spans the entire page? What happens?What if you have a very long string that spans the entire page? What happens?What if you have a very long string that spans the entire page? What happens?What if you have a very long string that spans the entire page? What happens?What if you have a very long string that spans the entire page? What happens?What if you have a very long string that spans the entire page? What happens?"
# print(very_long_string)

# very_long_string = '''What if you have a very long string that spans the entire page? What happens? 
# What if you have a very long string that spans the entire page? What happens?
# What if you have a very long string that spans the entire page? What happens?
# What if you have a very long string that spans the entire page? What happens?
# What if you have a very long string that spans the entire page? What happens?
# What if you have a very long string that spans the entire page? What happens?
# What if you have a very long string that spans the entire page? What happens?
# What if you have a very long string that spans the entire page? What happens?
# What if you have a very long string that spans the entire page? What happens?
# What if you have a very long string that spans the entire page? What happens?
# What if you have a very long string that spans the entire page? What happens?'''

# print(very_long_string)

# # Using backslash for line continuation? The backslash is an escape character.
# long_string = "Using a plus sign space backslash (\) " + \
#               "works good to. We do this for readability."
# print(long_string)

# # # What if we need to start with an empty string?
# empty_string = ""
# print(empty_string)
# print(type(empty_string))

# print(type(None))
#none_string = None
#print(none_string)
#print(type(none_string))
# string = "kim"
# print(type(string))
# #print(none_string, string)


# Let's talk about variable type names. It is a good time to do so.
# Starting with a number, using special characters is illegal (Note: underscore (_) is legal.)
# 8_five = 10

########################################################
# Exploration: 
# # 1) What is the result of using the plus sign with a string?
# # 2) Say you have one = "1" and two = "2", how do you get these to equal 3?
# # 3) What would you use to get a string to go to uppercase?
# # 4) What happens if you attempt to apply the function or method that make 'number' string lowercase (i.e. string = 1)?
# # 5) Is name = "Bob" the same as NAME = "Bob"? Prove it. What conclusions can you come up with about name and NAME? 
# # 6) Get the memory locations using id() - The identity of an object - memory address
# # 7) Is a string a mutable or immutable object?
# # 8) What is a variable name that is only uses capital letters?
# # 9) What is the difference between a constant and a variable?
# # 10) Try using 'while' as a variable name? What can you conclude?
# # 11) How do you find the length of a string?



# Here are the answers: 

#1) 
# name1 = "bob"
# name2 = "joe"
# print(name1, name2)
# print(name1 + name2)

#2) 
# one = "1"
# two = "2"
# print(one + two)
# print(int(one) + int(two))

#3) 
# string = "stop doing that!!!"
# print (string.upper())

#4) 
# string = '1'
# print(string.lower())

#5)
# name = "Bob"
# NAME = "Bob"
# # NAME = "Sue"
# # print (name, NAME)

# if name == NAME :
    
#     print(name)
#     print(NAME)
#     print(type(name))
#     print(type(NAME))


#6)
# print("Memory location of 'NAME':", id(NAME))
# print("Memory location of 'name':", id(name))

# Note: In some cases, Python might optimize memory usage by reusing the memory address for
# objects with the same value (like the string "Bob"), particularly for small immutable objects 
# like strings. However, the variables themselves (name and NAME) still exist at different locations 
# in memory even if their values are the same. You can confirm this by checking their id() values.

# If the id() values are the same, it's still possible that the variable names are separate entities, 
# but Python's memory optimization (such as string interning) could cause them to share the same memory 
# address for identical values. However, the important distinction here is that the variables themselves 
# are independent, and changing one will not affect the other.

#7) 
# immutable
# string = "string"
# print(type(string))
#8) 
# Constant

# 9) What is the difference between a constant and a variable?
# There is no enforcement of immutability (you can still change the value of a "constant"), 
# it's up to the developer to follow the naming convention and treat the value as a constant.
#10) 
# while = "August 12th"
# print (while)


# "What is the result of using the plus sign between two strings you are printing?", "the two strings are placed side by side with no space between them" 
# "What function would you used with one = '1' and two = '2' to get output 3?","the int function" 
# "What would you use to get a string to go to uppercase?", "use the upper method"
# "What happens if you attempt to apply the method lowercase to a string with numbers in it?", "the characters in the string are only changed to lowercase, numbers are not" 
# "How is name = 'Bob' and NAME = 'Bob'?", "there value is the same, they have the same memory location" 
# "How do you get the memory location of a variable", "use the function id, the identity of an object, its memory address"
# "Is a string a mutable or immutable object?", "immutable"
# "What is a variable name that is only uses capital letters?","a constant"
# "Is there any difference between the treatment of a constant and a variable in Python?", "no, it is up to the programmer how the constant is used"
# "Can we use reserved keywords as a variable name?", "no" 
# "How do you create a string literal?", "By either using single or double quotes"
# "What is used to create a multi-line strings?", "triple quotes or double quotes"
# "How do you find the type of an object?", "use the type function"
# "What is the function used to capitalize strings?", "capitalize"
# "What is the function used to capitalize every first letter of each word in a string?", "title"
# "What is the 'str' in the 'str.join()' method?", "it is the separator used between elements in the iterable"
# "If you use the 'str.join()' method on a set, what will the results be?", "sets are unordered collections you cannot guarantee the resulting string"

# book = "How The West Was Won"
# print(book.capitalize())
# print(book.title())

string1 = "I have"
string2 = "a mind of"
string3 = "my own."

result = ' '.join([string1, string2, string3])
print(result)

# result = ', '.join({string1, string2, string3})
# print(result)

# result = ', '.join((string1, string2, string3))
# print(result)

# result = " ".join("I have", "a mind of", "my own")
# print(result)

# number1 = "123"
# number2 = int("abc")
# print(number1)
# print(number2)

# string = "12345"
# print(string.isdigit())  

# string = "a1b2c3"
# print(string.isdigit())  

# string = "abcde"
# print(string.isdigit())  

# string = "12.34"
# print(string.isdigit())

# string = "-123"
# print(string.isdigit()) 

# # the 'in' operator: 
# main_string = "Hello, world!"
# substring = "world"

# # Check if substring exists in the main string
# if substring in main_string:
#     print("Substring found!")
# else:
#     print("Substring not found.")
    
# #Using the find() Method
# main_string = "Hello, world!"
# substring = "world"

# # Check if substring exists in the main string using find()
# position = main_string.find(substring)

# if position != -1:
#     print(f"Substring found at index {position}")
# else:
#     print("Substring not found.")
    

# #Using the index() Method
# main_string = "Hello, world!"
# substring = "world"

# try:
#     # Check if substring exists in the main string using index()
#     position = main_string.index(substring)
#     print(f"Substring found at index {position}")
# except ValueError:
#     print("Substring not found.")
    
# #Using Regular Expressions (with the re module)    
# import re

# main_string = "Hello, World!"
# substring = "world"

# # Check if substring exists in the main string using regular expressions (case-insensitive)
# if re.search(substring, main_string, re.IGNORECASE):
#     print("Substring found!")
# else:
#     print("Substring not found.")
    
# # Example with lowercase letter 'a'
# ascii_value = 97
# character = chr(ascii_value)
# print(character)

#11

print(len("Python"))



