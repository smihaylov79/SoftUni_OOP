def logged(fn):
    def wrapper(*args):
        result=fn(*args)
        return f"you called {fn.__name__}{args}\nit returned {result}"
    return wrapper





@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))


print()

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))