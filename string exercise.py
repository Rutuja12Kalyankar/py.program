my_string = """In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. The latter may allow its elements to be mutated and the length changed, or it may be fixed (after creation). A string is generally considered as a data type and is often implemented as an array data structure of bytes (or words) that stores a sequence of elements, typically characters, using some character encoding. String may also denote more general arrays or other sequence (or list) data types and structures.
Depending on the programming language and precise data type used, a variable declared to be a string may either cause storage in memory to be statically allocated for a predetermined maximum length or employ dynamic allocation to allow it to hold a variable number of elements."""

# WAP in python to count total number of words in given paragraph

words = my_string.split()
word_count = len(words)
print(word_count)

# WAP to change case of string to STRING(use of loop)

upper_case_string = ""
for char in my_string:
    upper_case_string += char.upper()
print(upper_case_string)

# WAP to separate lines in given paragraph

lines = my_string.splitlines()
for line in lines:
    print(lines)

 # WAP to print no of lines present in given paragraph 
lines = my_string.splitlines()
line_count = len(lines)

print("number of lines in my_string: " ,line_count)

# WAP to replace “string” with “string in python”(use replace())

new_string = my_string.replace("string", "string in python")
print(new_string)

# WAP to replace all ‘s’ with ‘p’(replace())
new_string = my_string.replace("s", "p")
print(new_string)