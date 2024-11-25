class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = tuple(dictionary.items())
        self.i=0

    def __iter__(self):
        return self
        # return iter(self.dictionary.items())

    def __next__(self):
        if self.i<len(self.dictionary):
            i=self.i
            self.i+=1
            return self.dictionary[i]
        raise StopIteration

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
