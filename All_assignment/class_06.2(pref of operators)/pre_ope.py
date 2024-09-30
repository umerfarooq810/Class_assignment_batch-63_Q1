

# Parentheses
a = 5
b = 10
c = 2
result = (a + b) * c  # Using parentheses to change the order of operations
print("Result with parentheses:", result)

# Exponentiation
exponent_result = a ** c  # 5 raised to the power of 2
print("Exponentiation result (5 ** 2):", exponent_result)  

# Unary operators
unary_plus = +a  # Unary plus (has no effect)
unary_minus = -b  # Unary minus (negates b)
print("Unary plus (5):", unary_plus)
print("Unary minus (10):", unary_minus)

# Multiplication, Division, Modulus, Floor Division
mul_result = a * b  # Multiplication
div_result = b / c  # Division
mod_result = b % c  # Modulus (remainder)
floor_div_result = b // c  # Floor Division
print("Multiplication (5 * 10):", mul_result)
print("Division (10 / 2):", div_result)
print("Modulus (10 % 2):", mod_result)
print("Floor Division (10 // 2):", floor_div_result)

# Addition and Subtraction
add_result = a + b  # Addition
sub_result = b - a  # Subtraction
print("Addition (5 + 10):", add_result)
print("Subtraction (10 - 5):", sub_result)

# Comparisons
comparison_eq = (a == b)  # Equal to
comparison_neq = (a != b)  # Not equal to
comparison_gt = (a > b)  # Greater than
comparison_lt = (a < b)  # Less than
print("Comparison (5 == 10):", comparison_eq)  # Output: False
print("Comparison (5 != 10):", comparison_neq)  # Output: True
print("Comparison (5 > 10):", comparison_gt)  # Output: False
print("Comparison (5 < 10):", comparison_lt)  # Output: True

# Boolean NOT, AND, OR
bool_a = True
bool_b = False
not_result = not bool_a  # Negation
and_result = bool_a and bool_b  # Logical AND
or_result = bool_a or bool_b  # Logical OR
print("Boolean NOT (not True):", not_result)  # Output: False
print("Boolean AND (True and False):", and_result)  # Output: False
print("Boolean OR (True or False):", or_result)  # Output: True

# Assignment Operators
x = 5
x += 3  # x = x + 3
print("After += (x += 3):", x)  # Output: 8
x *= 2  # x = x * 2
print("After *= (x *= 2):", x)  # Output: 16

# Lambda expressions
add_lambda = lambda y: y + 2  # A simple lambda function that adds 2 to the input
lambda_result = add_lambda(5)  # Call the lambda function with 5
print("Lambda result (add_lambda(5)):", lambda_result)  # Output: 7

print()

# Operator Precedence Demonstration in Python

# 1. Parentheses () - highest precedence
result_1 = (5 + 3) * 2
print("Result of (5 + 3) * 2:", result_1)

# 2. Exponentiation (**) - higher precedence than multiplication
result_2 = 2 ** 3 * 4
print("Result of 2 ** 3 * 4:", result_2)

# 3. Unary plus and minus, and bitwise NOT
result_3 = -5 + 3
print("Result of -5 + 3:", result_3)

# 4. Multiplication (*), Division (/), Floor Division (//), and Modulus (%)
result_4 = 10 * 2 // 3 % 2
print("Result of 10 * 2 // 3 % 2:", result_4)

# 5. Addition and Subtraction (+, -)
result_5 = 10 - 2 + 4
print("Result of 10 - 2 + 4:", result_5)

# 6. Comparison Operators (==, !=, >, <, >=, <=)
result_6 = 10 > 5 and 5 < 3
print("Result of 10 > 5 and 5 < 3:", result_6)

# 7. Boolean operators (not, and, or)
result_7 = not (10 == 10 or 5 != 3)
print("Result of not (10 == 10 or 5 != 3):", result_7)

# 8. Assignment operators (=, +=, -=, etc.)
x = 5
x += 3  # Same as x = x + 3, so x becomes 8
print("Result of x += 3 when x starts as 5:", x)


