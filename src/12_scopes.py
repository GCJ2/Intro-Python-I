# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def change_x():
    global x    # This brings in the global variable into local scope
    x = 99      # Anything we do to x now changes the x global variable


change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
# Bring global x into the scope of the function so the global variable can be affected
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y  # While y is not global, but it is nonlocal, so we can bring it in this way
        y = 999     # Reassign the value to 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()
