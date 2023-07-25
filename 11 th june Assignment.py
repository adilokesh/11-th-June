#!/usr/bin/env python
# coding: utf-8

# # Q1. What is a lambda function in Python, and how does it differ from a regular function?

# Lambda functions are anonymous functions that are defined using the lambda keyword. They can have any number of arguments but only one expression, which is evaluated and returned. Lambda functions are mainly used as a convenient way to create simple and short functions that are not needed later in the code.
# 
# Regular functions are named functions that are defined using the def keyword. They can have any number of arguments and statements, and they can return any Python object. Regular functions are mainly used to create reusable and modular code that can be called multiple times in the code.
# 
# The main differences between lambda functions and regular functions are:
# 
# Lambda functions are anonymous, while regular functions have a name. Lambda functions are defined on a single line, while regular functions can span multiple lines. Lambda functions can only have one expression, while regular functions can have multiple statements. Lambda functions do not support docstrings, while regular functions can have documentation strings. Lambda functions cannot use global or nonlocal statements, while regular functions can.

# # Q2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use them?

# Yes, a lambda function in Python can have multiple arguments. You can define and use them by separating the arguments by commas after the lambda keyword and before the colon. For example:

# In[2]:


# Define a lambda function that takes two arguments and returns their sum
add = lambda x, y: x + y

# Call the lambda function with some values
result = add(3, 4)
print(result) # 7


# In this example, we define a lambda function that takes two arguments (x and y) and returns their sum (x + y). We assign the lambda function to a variable (add) and call it with some values (3 and 4). The result is printed as 7.
# 
# You can also use a lambda function with multiple arguments as an argument to another function that expects a function object, such as map(), filter(), or sorted(). For example:

# In[1]:


# Define two lists of numbers
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]

# Use a lambda function with two arguments to add the corresponding elements of the lists
result = list(map(lambda x, y: x + y, numbers1, numbers2))
print(result) # [6, 8, 10, 12]


# # Q3. How are lambda functions typically used in Python? Provide an example use case.

# Lambda functions are typically used in Python to create simple and anonymous functions that can be passed as arguments to other functions or returned as values. Lambda functions are useful when you need a short and concise function that is only used once or a few times in your code.
# 
# Some common use cases of lambda functions in Python are:
# 
# 1. When using built-in functions, such as map(), filter(), and reduce(), that take a function object as an argument and apply it to an iterable. 

# 2. When sorting Python data structures, such as lists and dictionaries, by using a custom key function.

# 3. When creating small, one-time-use functions that perform simple tasks

# 4. When implementing simple event handlers for graphical user interfaces (GUIs) or web frameworks.

# # Q4. What are the advantages and limitations of lambda functions compared to regular functions in Python?

# Some of the advantages and limitations of lambda functions compared to regular functions in Python are:
# 
# ### Advantages:
# 
# Lambda functions can be written in a concise and elegant way, without using the def and return keywords. This can make the code more readable and expressive, especially when using lambda functions as arguments to other functions.
# Lambda functions can be created and executed on the fly, without needing to assign them to a variable or give them a name. This can be useful for creating one-time-use functions that perform simple tasks.
# Lambda functions can access the variables from the enclosing scope, which can be handy for creating closures or decorators.
# 
# ### Limitations:
# 
# Lambda functions can only contain one expression, which means they cannot have multiple statements or complex logic. This can limit their functionality and make them less versatile than regular functions.
# Lambda functions do not support docstrings, which means they cannot have documentation or comments. This can make them harder to understand and debug, especially for complex or obscure expressions.
# Lambda functions are anonymous, which means they cannot be referenced by name or reused later in the code. This can make them less flexible and modular than regular functions.
# I hope this helps you understand the advantages and limitations of lambda functions in Python. 

# # Q5. Are lambda functions in Python able to access variables defined outside of their own scope? Explain with an example.

# Yes, lambda functions in Python are able to access variables defined outside of their own scope. This is because lambda functions can use the variables from the enclosing scope, which is the region of code where the lambda function is defined12
# 
# For example, consider the following code:

# In[5]:


# Define a variable outside the lambda function
x = 10

# Define a lambda function that uses the variable x
f = lambda y: x + y

# Call the lambda function with some value
print(f(5)) # 15


# In this example, the lambda function f uses the variable x, which is defined outside of its own scope. The lambda function can access x because it is in the enclosing scope of the lambda function. The output is 15, which is the result of adding x (10) and y (5).
# 
# However, there are some caveats to be aware of when using variables from the outer scope in lambda functions. For example:
# 
# If the variable is mutable, such as a list or a dictionary, then modifying it inside the lambda function will affect the original object in the outer scope.
# If the variable is immutable, such as a number or a string, then assigning a new value to it inside the lambda function will create a new local variable that shadows the outer variable. The original object in the outer scope will not be affected.
# If the variable is defined in a loop or a comprehension, then it may have a different value than expected when the lambda function is executed. This is because the variable will have its final value from the loop or comprehension, not the value at each iteration. To avoid this, you can use default arguments to bind the variable to the lambda function.

# In[6]:


# Define a mutable variable outside the lambda function
my_list = [1, 2, 3]

# Define a lambda function that modifies the variable my_list
g = lambda z: my_list.append(z)

# Call the lambda function with some value
g(4)

# Print the variable my_list
print(my_list) # [1, 2, 3, 4]


# In this example, the lambda function g modifies the variable my_list, which is defined outside of its own scope. The lambda function can access and modify my_list because it is a mutable object in the enclosing scope of the lambda function. The output is [1, 2, 3, 4], which shows that my_list has been changed by g.

# # Q6. Write a lambda function to calculate the square of a given number.

# To write a lambda function to calculate the square of a given number, you can use the following syntax:
# 

# In[9]:


# Define a lambda function that takes a number as an argument and returns its square
square = lambda x: x ** 2

# Call the lambda function with some value
print(square(5)) # 25


# In this example, we define a lambda function that takes a number (x) as an argument and returns its square (x ** 2). We assign the lambda function to a variable (square) and call it with some value (5). The output is 25, which is the result of squaring 5.

# # Q7. Create a lambda function to find the maximum value in a list of integers.

# In[10]:


# Define a lambda function that takes a number as an argument and returns its square
square = lambda x: x ** 2

# Call the lambda function with some value
print(square(5)) # 25


# In this example, we define a lambda function that takes a number (x) as an argument and returns its square (x ** 2). We assign the lambda function to a variable (square) and call it with some value (5). The output is 25, which is the result of squaring 5.

# # Q8. Implement a lambda function to filter out all the even numbers from a list of integers.

# To implement a lambda function to filter out all the even numbers from a list of integers, you can use the built-in filter() function, which returns an iterator of the elements of an iterable for which a function returns True. You can pass the list of integers as an iterable and a lambda expression as a function to the filter() function. The lambda expression should check if each element is divisible by 2 and return True if it is not (i.e., if it is odd)

# In[11]:


# Define a list of integers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# To filter out all the even numbers from this list, you can use the filter() function with a lambda expression as follows:
# 
# 

# In[12]:


# Filter out all the even numbers from the list
odd_numbers = filter(lambda x: x % 2 != 0, my_list)

# Convert the filter object to a list
odd_numbers = list(odd_numbers)

# Print the list of odd numbers
print(odd_numbers) # [1, 3, 5, 7, 9]


# In this example, we use the filter() function with a lambda expression that takes an element (x) as an argument and returns True if x % 2 is not equal to 0 (i.e., if x is odd). This will filter out all the even numbers from the list and return a filter object. We then convert the filter object to a list and print it as [1, 3, 5, 7, 9].
# 
# I hope this helps you understand how to implement a lambda function to filter out all the even numbers from a list of integers.

# # Q9. Write a lambda function to sort a list of strings in ascending order based on the length of each string.

# To write a lambda function to sort a list of strings in ascending order based on the length of each string, you can use the built-in sorted() function, which returns a new sorted list from an iterable. You can pass the list of strings as an iterable and a lambda expression as a key function to the sorted() function. The key function should return the length of each string, which will be used as the basis for sorting

# In[13]:


# Define a list of strings
my_list = ["apple", "banana", "cherry", "date"]


# To sort this list in ascending order based on the length of each string, you can use the sorted() function with a lambda expression as follows:

# In[15]:


# Sort the list in ascending order based on the length of each string
sorted_list = sorted(my_list, key=lambda x: len(x))

# Print the sorted list
print(sorted_list) # ['date', 'apple', 'banana', 'cherry']


# In this example, we use the sorted() function with a lambda expression that takes a string (x) as an argument and returns its length (len(x)). This will sort the list in ascending order based on the length of each string and return a new sorted list. We then print the sorted list as [‘date’, ‘apple’, ‘banana’, ‘cherry’].
# 
# I hope this helps you understand how to write a lambda function to sort a list of strings in ascending order based on the length of each string.

# # Q10. Create a lambda function that takes two lists as input and returns a new list containing the common elements between the two lists.
To create a lambda function that takes two lists as input and returns a new list containing the common elements between the two lists, you can use the built-in filter() function, which returns an iterator of the elements of an iterable for which a function returns True. You can pass a lambda expression as a function and one of the lists as an iterable to the filter() function. The lambda expression should check if each element is present in the other list and return True if it is.

For example, suppose you have two lists like this:
# In[16]:


# Define two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]


# To create a lambda function that returns a new list containing the common elements between these two lists, you can use the filter() function with a lambda expression as follows:

# In[17]:


# Create a lambda function that takes two lists as input and returns a new list containing the common elements
common_elements = lambda l1, l2: list(filter(lambda x: x in l2, l1))

# Call the lambda function with the two lists
result = common_elements(list1, list2)

# Print the result
print(result) # [3, 4, 5]


# In this example, we create a lambda function that takes two lists (l1 and l2) as input and returns a new list containing the common elements. We use the filter() function with a lambda expression that takes an element (x) as an argument and returns True if x is in l2 (i.e., if x is a common element). This will filter out all the elements that are not in both lists and return a filter object. We then convert the filter object to a list and assign it to result. We then print the result as [3, 4, 5].
# 
# I hope this helps you understand how to create a lambda function that takes two lists as input and returns a new list containing the common elements between the two lists.

# # Q11. Write a recursive function to calculate the factorial of a given positive integer.

# To write a recursive function to calculate the factorial of a given positive integer, you can use the following logic:
# 
# Define a function that takes an integer n as an argument.
# Check if n is equal to 0 or 1, which are the base cases. If so, return 1 as the factorial of 0 or 1.
# Otherwise, return n multiplied by the result of calling the same function with n - 1 as the argument. This is the recursive step, which reduces the problem size by one at each call.
# Make sure to handle invalid inputs, such as negative numbers or non-integers, by printing an error message or raising an exception.
# For example, you can write the recursive function to calculate the factorial of a given positive integer in Python as follows:

# In[18]:


# Define a recursive function to calculate the factorial of a given positive integer
def factorial(n):
  # Check if n is a valid positive integer
  if not isinstance(n, int) or n < 0:
    print("Invalid input. Please enter a positive integer.")
    return None
  # Check if n is 0 or 1, which are the base cases
  elif n == 0 or n == 1:
    return 1
  # Otherwise, return n multiplied by the result of calling the same function with n - 1
  else:
    return n * factorial(n - 1)

# Call the function with some values
print(factorial(5)) # 120
print(factorial(10)) # 3628800
print(factorial(-3)) # Invalid input. Please enter a positive integer.
print(factorial(3.5)) # Invalid input. Please enter a positive integer.


# In this example, we define a recursive function that takes an integer n as an argument and returns the factorial of that number. We first check if n is a valid positive integer, and print an error message and return None if it is not. We then check if n is 0 or 1, which are the base cases, and return 1 as the factorial of 0 or 1. Otherwise, we return n multiplied by the result of calling the same function with n - 1 as the argument, which is the recursive step. We then call the function with some values and print the results.

# # Q12. Implement a recursive function to compute the nth Fibonacci number.

# To implement a recursive function to compute the nth Fibonacci number, you can use the following logic:
# 
# Define a function that takes an integer n as an argument.
# Check if n is equal to 0 or 1, which are the base cases. If so, return n as the nth Fibonacci number.
# Otherwise, return the sum of calling the same function with n - 1 and n - 2 as the arguments. This is the recursive step, which follows the definition of the Fibonacci sequence: F(n) = F(n - 1) + F(n - 2).
# Make sure to handle invalid inputs, such as negative numbers or non-integers, by printing an error message or raising an exception.
# For example, you can write the recursive function to compute the nth Fibonacci number in Python as follows:

# In[19]:


# Define a recursive function to compute the nth Fibonacci number
def fibonacci(n):
  # Check if n is a valid positive integer
  if not isinstance(n, int) or n < 0:
    print("Invalid input. Please enter a positive integer.")
    return None
  # Check if n is 0 or 1, which are the base cases
  elif n == 0 or n == 1:
    return n
  # Otherwise, return the sum of calling the same function with n - 1 and n - 2
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

# Call the function with some values
print(fibonacci(5)) # 5
print(fibonacci(10)) # 55
print(fibonacci(-3)) # Invalid input. Please enter a positive integer.
print(fibonacci(3.5)) # Invalid input. Please enter a positive integer.


# In this example, we define a recursive function that takes an integer n as an argument and returns the nth Fibonacci number. We first check if n is a valid positive integer, and print an error message and return None if it is not. We then check if n is 0 or 1, which are the base cases, and return n as the nth Fibonacci number. Otherwise, we return the sum of calling the same function with n - 1 and n - 2 as the arguments, which is the recursive step. We then call the function with some values and print the results.

# # Q13. Create a recursive function to find the sum of all the elements in a given list.

# To create a recursive function to find the sum of all the elements in a given list, you can use the following logic:
# 
# Define a function that takes a list as an argument.
# Check if the list is empty, which is the base case. If so, return 0 as the sum of an empty list.
# Otherwise, return the first element of the list plus the result of calling the same function with the rest of the list as the argument. This is the recursive step, which reduces the problem size by one at each call.
# Make sure to handle invalid inputs, such as non-lists or lists containing non-numbers, by printing an error message or raising an exception.

# In[20]:


# Define a recursive function to find the sum of all the elements in a given list
def list_sum(lst):
  # Check if lst is a valid list of numbers
  if not isinstance(lst, list) or not all(isinstance(x, (int, float)) for x in lst):
    print("Invalid input. Please enter a list of numbers.")
    return None
  # Check if lst is empty, which is the base case
  elif not lst:
    return 0
  # Otherwise, return the first element plus the result of calling the same function with the rest of the list
  else:
    return lst[0] + list_sum(lst[1:])

# Call the function with some values
print(list_sum([1, 2, 3, 4, 5])) # 15
print(list_sum([-1, 0.5, 2.5])) # 2.0
print(list_sum([])) # 0
print(list_sum(3)) # Invalid input. Please enter a list of numbers.
print(list_sum([1, "a", 3])) # Invalid input. Please enter a list of numbers.


# # Q14. Write a recursive function to determine whether a given string is a palindrome.

# To write a recursive function to determine whether a given string is a palindrome, you can use the following logic:
# 
# Define a function that takes a string as an argument.
# Check if the string is empty or has one character, which are the base cases. If so, return True as the string is a palindrome.
# Otherwise, check if the first and last characters of the string are equal. If not, return False as the string is not a palindrome.
# Otherwise, return the result of calling the same function with the substring that excludes the first and last characters. This is the recursive step, which reduces the problem size by two at each call.
# Make sure to handle invalid inputs, such as non-strings, by printing an error message or raising an exception.

# In[22]:


# Define a recursive function to determine whether a given string is a palindrome
def is_palindrome(s):
  # Check if s is a valid string
  if not isinstance(s, str):
    print("Invalid input. Please enter a string.")
    return None
  # Check if s is empty or has one character, which are the base cases
  elif len(s) <= 1:
    return True
  # Check if the first and last characters of s are equal
  elif s[0] != s[-1]:
    return False
  # Otherwise, return the result of calling the same function with the substring that excludes the first and last characters
  else:
    return is_palindrome(s[1:-1])

# Call the function with some values
print(is_palindrome("racecar")) # True
print(is_palindrome("madam")) # True
print(is_palindrome("hello")) # False
print(is_palindrome(123)) # Invalid input. Please enter a string.


# # Q15. Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.

# In[23]:


# Define a recursive function to find the GCD of two positive integers
def gcd(a, b):
  # Check if a and b are valid positive integers
  if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
    print("Invalid input. Please enter two positive integers.")
    return None
  # Check if b is 0, which is the base case
  elif b == 0:
    return a
  # Otherwise, return the result of calling the same function with b and the remainder of a divided by b
  else:
    return gcd(b, a % b)

# Call the function with some values
print(gcd(12, 18)) # 6
print(gcd(60, 36)) # 12
print(gcd(-3, 5)) # Invalid input. Please enter two positive integers.
print(gcd(3.5, 7)) # Invalid input. Please enter two positive integers.


# In this example, we define a recursive function that takes two integers (a and b) as arguments and returns the GCD of them. We first check if a and b are valid positive integers, and print an error message and return None if they are not. We then check if b is 0, which is the base case, and return a as the GCD of a and b. Otherwise, we return the result of calling the same function with b and the remainder of a divided by b (a % b) as the arguments, which is the recursive step. We then call the function with some values and print the results.

# In[ ]:




