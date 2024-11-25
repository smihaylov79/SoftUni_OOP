def read_next(*args):
    for item in args:
        for el in item:
            yield el


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

