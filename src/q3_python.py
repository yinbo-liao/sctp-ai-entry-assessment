# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName):
    #use f-string to format the name in the format "lastName, firstName"
    return f"{lastName}, {firstName}"


# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
def formatInitials(firstName, lastName):
    #use f-string to format the initials of the person in uppercase
    return f"{firstName[0].upper()}.{lastName[0].upper()}"


# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):
    # use f-string to format the initials of the person in uppercase
    return f"{firstName[0].upper()}.{lastName[0].upper()}"


# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):
    # use f-string to format the initials of the person in uppercase

    return f"{firstName[0].upper()}.{lastName[0].upper()}"


# Task 3:
# Call both functions with the following inputs and print each result:
#   formatName("Alice", "Tan")  → Expected: "Tan, Alice"
#   formatName("bob", "lim")    → Expected: "Lim, Bob"
#   formatInitials("Alice","Tan") → Expected: "A.T."
#   formatInitials("bob","lim")   → Expected: "B.L."
 
# Add your code here
#call formatName function with the inputs and print the results
print(formatName("Alice", "Tan"))

print(formatName("bob", "lim"))
#call formatInitials function with the inputs and print the results
print(formatInitials("Alice", "Tan"))

print(formatInitials("bob", "lim"))
