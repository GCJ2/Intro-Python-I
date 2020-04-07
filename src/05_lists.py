# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)     # Adds item to end of list
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)     # Adds elements of any iterable to end of current list
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)     # Removes first element with passed value
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(len(x) - 1, 99)    # At a specific position, add a specific element
print(x)

# Print the length of list x
# YOUR CODE HERE
for i in x:     # For every object in x
    print(i)    # Print it

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:             # For every object in x
    print(i * 1000)     # Multiply it by 1000
