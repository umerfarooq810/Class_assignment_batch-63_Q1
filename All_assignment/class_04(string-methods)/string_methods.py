# 1. capitalize() Capitalizes the first character of the string.
text = "hello, world!"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: Hello, world!

# 2. casefold() Converts the string to lowercase for caseless comparisons.

text = "HELLO WORLD"
casefolded_text = text.casefold()
print(casefolded_text)  # Output: hello world

# 3. center() Returns a centered string of a specified length.

text = "hello"
centered_text = text.center(10, "*")
print(centered_text)  # Output: ***hello***

# 4. count() Returns the number of occurrences of a substring.

text = "banana"
count_a = text.count("a")
print(count_a)  # Output: 3

# 5. encode() Encodes the string into a bytes object using a specified encoding.

text = "hello"
encoded_text = text.encode("utf-8")
print(encoded_text)  # Output: b'hello'

# 6. endswith() Checks if the string ends with a specified suffix.

text = "hello, world!"
ends_with_world = text.endswith("world!")
print(ends_with_world)  # Output: True
# 7. expandtabs() Replaces tabs with spaces.

text = "hello\tworld"
expanded_text = text.expandtabs(4)
print(expanded_text)  # Output: hello    world

# 8. find() Returns the index of the first occurrence of a substring.

text = "hello, world!"
index = text.find("world")
print(index)  # Output: 7

# 9. format() Formats a string using placeholders.

name = "Alice"
age = 30
formatted_string = "Hello, my name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: Hello, my name is Alice and I am 30 years old.

# 10. format_map() Formats a string using a mapping.

values = {'name': 'Alice', 'age': 30}
formatted_string = "Hello, my name is {name} and I am {age} years old.".format_map(values)
print(formatted_string)  # Output: Hello, my name is Alice and I am 30 years old

# 11. index() Returns the index of the first occurrence of a substring, raising a ValueError if not found.

text = "hello, world!"
index = text.index("world")
print(index)  # Output: 7

# 12. isalnum() Returns True if all characters are alphanumeric.

text = "hello123"
is_alnum = text.isalnum()
print(is_alnum)  # Output: True

# 13. isalpha() Returns True if all characters are alphabetic.

text = "hello"
is_alpha = text.isalpha()
print(is_alpha)  # Output: True

# 14. isascii() Returns True if all characters are ASCII.

text = "hello"
is_ascii = text.isascii()
print(is_ascii)  # Output: True

# 15. isdecimal() Returns True if all characters are decimal digits.

text = "123"
is_decimal = text.isdecimal()
print(is_decimal)  # Output: True

# 16. isdigit() Returns True if all characters are digits.

text = "123"
is_digit = text.isdigit()
print(is_digit)  # Output: True

# 17. isidentifier() Returns True if the string is a valid identifier.

text = "my_variable"
is_identifier = text.isidentifier()
print(is_identifier)  # Output: True

# 18. islower() Returns True if all characters are lowercase.

text = "hello"
is_lower = text.islower()
print(is_lower)  # Output: True

# 19. isnumeric() Returns True if all characters are numeric.

text = "123"
is_numeric = text.isnumeric()
print(is_numeric)  # Output: True

# 20. isprintable() Returns True if all characters are printable.

text = "hello world"
is_printable = text.isprintable()
print(is_printable)  # Output: True

# 21. isspace() Returns True if all characters are whitespace.

text = "  \t\n"
is_space = text.isspace()
print(is_space)  # Output: True

# 22. istitle() Returns True if the string is a titlecased string.

text = "Hello, World!"
is_title = text.istitle()
print(is_title)  # Output: True

# 23. isupper() Returns True if all characters are uppercase.

text = "HELLO"
is_upper = text.isupper()
print(is_upper)  # Output: True

# 24. join() Concatenates elements of an iterable into a string.

words = ["hello", "world"]
text = " ".join(words)
print(text)  # Output: hello world

# 25. ljust() Returns a left-justified string of a specified length.

text = "hello"
left_justified = text.ljust(10, "*")
print(left_justified)  # Output: hello*****

# 26. lower() Converts all characters to lowercase.

text = "HELLO"
lower_text = text.lower()
print(lower_text)  # Output: hello

# 27. lstrip() Removes leading whitespace from the string.

text = "  hello, world!  "
stripped_text = text.lstrip()
print(stripped_text)  # Output: hello, world!  

# 28. maketrans() Creates a translation table for use with the translate() method.

translation_table = str.maketrans("aeiou", "12345")
text = "hello"
translated_text = text.translate(translation_table)
print(translated_text)  # Output: h1ll0

# 29. partition() Splits the string into a tuple of three parts based on the first occurrence of a separator.

text = "hello, world!"
parts = text.partition(" ")
print(parts)  # Output: ('hello', ', ', 'world!')

# 30. removeprefix() Removes a prefix from the string if it exists.

text = "hello world"
removed_prefix = text.removeprefix("hello ")
print(removed_prefix)  # Output: world

# 31. removesuffix() Removes a suffix from the string if it exists.

text = "hello world!"
removed_suffix = text.removesuffix(" world!")
print(removed_suffix)  # Output: hello

# 32. replace() Replaces occurrences of a substring with another substring.

text = "hello, world!"
replaced_text = text.replace("world", "Python")
print(replaced_text)  # Output: Hello, Python!

# 33. rfind() Returns the index of the last occurrence of a substring.

text = "hello, world, hello"
index = text.rfind("hello")
print(index)  # Output: 14

# 34. rindex() Returns the index of the last occurrence of a substring, raising a ValueError if not found.

text = "hello, world, hello,"
index = text.rindex("world")
print(index)  # Output: 7

