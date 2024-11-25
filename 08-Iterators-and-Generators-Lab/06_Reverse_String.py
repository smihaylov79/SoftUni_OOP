def reverse_text(string):
    for i in range(len(string),0,-1):
        yield string[i-1]


for char in reverse_text("step"):
    print(char, end='')
