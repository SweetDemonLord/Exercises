print("Let's start generating code")
# Creating an exception object
error=Exception("The first error")
# The first scope of the controlled code
try:
    # The second scope of the controlled code
    try:
        # The third scope of the controlled code
        try:
            # Generating an exception
            raise error
        # Exception handling for the third scope
        except:
            print(error)
            # Re-generating an exception
            raise
    # Exception handling for the second scope
    except Exception as e:
        print("Reprocessing")
        print(e)
        # Inner scope of the controlled code
        try:
            # Generating an exception
            raise ArithmeticError("The second error")
        # Exception handling for the inner scope
        except ArithmeticError as e:
            print(e)
        # Generating an exception
        raise Warning
# Exception handling for the first scope
except Warning:
    print("One more error")
print("No more errors")