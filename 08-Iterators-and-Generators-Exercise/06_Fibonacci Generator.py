def fibonacci():
    current_number = 0
    next_number = 1
    while True:
        yield current_number
        current_number , next_number = next_number, current_number + next_number


generator = fibonacci()
for i in range(125):
    print(next(generator))
