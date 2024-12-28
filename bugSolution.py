def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        if isinstance(b, str):
            return "Cannot divide by a string"
        else:
            return "Type Error: Unexpected data type"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

print(function_with_uncommon_error(10,0))
print(function_with_uncommon_error(10,'a'))
print(function_with_uncommon_error(10,2))