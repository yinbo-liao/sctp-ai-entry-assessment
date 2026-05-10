# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Task 1:
# Declare an empty list called inventory to store item names as strings.

# Add your code here
#create an empty list called inventory
inventory = []

# Task 2:
# Write a function called addItem(itemName) that adds the given item to the
# inventory list. If the item already exists, print a message instead of adding it.
# Example message: "Mouse is already in inventory."
""" (empty string);
[] (empty list);
{} (empty dict);
() (empty tuple);
set() (empty set);
0;
None;
False are considered "falsy" values in Python"""

def addItem(itemName):
    #iterate through inventory to check if itemName already exists
    if itemName not in inventory:
        #add itemName to inventory if it does not exist
        inventory.append(itemName) 
    else:
        # Item already exists, print a message
        print(f"{itemName} is already in inventory.")

# Task 3:
# Write a function called listInventory() that prints all items in the inventory.
# If the inventory is empty, print: "Inventory is empty."
def listInventory():
    # Check if inventory is empty
    if not inventory:
        print("Inventory is empty.")
    else:
        # Print all items in the inventory
        for item in inventory:
            print(item)


# Task 4:
# Call the functions in this order and observe the output:
#addItem("Laptop","Mouse","Keyboard") to add "Laptop" to the inventory
addItem("Laptop")
addItem("Mouse")
addItem("Keyboard")
addItem("Mouse")   # Should trigger duplicate warning
# Call listInventory() to print the current inventory
listInventory()

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']
