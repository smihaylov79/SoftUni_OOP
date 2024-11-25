def type_check(param_type):
    def decorator(func):
        def wrapper(p):
            if not isinstance(p, param_type):
                return 'Bad Type'
            return func(p)
        return wrapper
    return decorator



@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

