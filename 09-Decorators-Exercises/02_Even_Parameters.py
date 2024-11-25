def even_parameters(fn):
    def wrapper(*args, **kwargs):
        if any(not isinstance(el, int) or el%2!=0 for el in args):
            return f"Please use only even numbers!"
        return fn(*args, **kwargs)
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

print("++++")


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
