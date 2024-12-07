def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

print(function_with_uncommon_error(2))  # Output: 5.0
print(function_with_uncommon_error(0))  # Output: Division by zero
print(function_with_uncommon_error('a')) # Output: Invalid input type

# Uncommon Error: Ignoring a Specific Exception Type
# The function handles ZeroDivisionError and TypeError, but it doesn't handle other potential exceptions like ValueError (if x is a string that can't be converted to a number).
# This could be improved by either implementing a more robust try...except block or by adding input validation to prevent unexpected exceptions.
# An even better approach is to add input validation before the try-except block and raise a more specific exception.