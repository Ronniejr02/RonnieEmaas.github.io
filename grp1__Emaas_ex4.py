# Part 1: If statement returning True or False
def check_number(num):
    if num > 10:
        return True
    else:
        return False

# Example usage of the if condition
number = 15
result = check_number(number)
print(f"Is {number} greater than 10? {result}")

# Part 2: List, Tuples, Sets, and Dictionaries with String, int, and boolean data types

# List
my_list = ["apple", 5, True]
print("List:", my_list)

# Tuple
my_tuple = ("banana", 10, False)
print("Tuple:", my_tuple)

# Set
my_set = {"cherry", 15, True}
print("Set:", my_set)

# Dictionary
my_dict = {
    "name": "Ronnie",
    "age": 21,
    "is_student": True
}
print("Dictionary:", my_dict)

# Accessing elements from each collection
print("First element in list:", my_list[0])  # Accessing list element
print("Second element in tuple:", my_tuple[1])  # Accessing tuple element
print("Checking if 'cherry' is in set:", "cherry" in my_set)  # Checking set membership
print("Name in dictionary:", my_dict["name"])  # Accessing dictionary value
