
#Exercise 1
def calculate(a, b=10, c=None):
    if c is None:
        print(a + b)
    else:
        print(a * b * c)

# Example usage:
calculate(5)        # Output: 15 (5 + 10)
calculate(5, 3)     # Output: 8 (5 + 3)
calculate(5, 3, 2)  # Output: 30 (5 * 3 * 2)


#exercise 2
def filter_strings_by_length(strings):
    return [s for s in strings if len(s) >= 5]

# Example usage:
strings = ["apple", "cat", "banana", "dog", "elephant"]
print(filter_strings_by_length(strings))  # Output: ['apple', 'banana', 'elephant']


#Exercise 3
expression = "3 * 5 + 2"
result = eval(expression)
print(result)  # Output: 17



# Exercise 4

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(numbers):
    return list(filter(is_prime, numbers))

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filter_primes(numbers))  # Output: [2, 3, 5, 7]




#Exercise 5
def convert_to_uppercase(strings):
    return list(map(str.upper, strings))

# Example usage:
strings = ["hello", "world", "python"]
print(convert_to_uppercase(strings))  # Output: ['HELLO', 'WORLD', 'PYTHON']

