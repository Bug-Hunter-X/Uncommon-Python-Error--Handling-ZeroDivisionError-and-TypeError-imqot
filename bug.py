def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type Error"

print(function_with_uncommon_error(10,0))
print(function_with_uncommon_error(10,'a'))
print(function_with_uncommon_error(10,2))