def outer_function(x):
    # This is the outer function
    def inner_function(y):
        # This is the nested (inner) function
        return y ** 2
    result = inner_function(x)
    return result + 10 # Adds 10 to the result of the inner function
# Using the outer function
value = 5
output = outer_function(value)
print("The result is:", output)