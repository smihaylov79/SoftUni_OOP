class vowels:
    def __init__(self,string):
        self.string = string
        self.vowels=[el for el in self.string if el.lower() in ['a','e','i','o','u', 'y']]
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index < len(self.vowels):
            return self.vowels[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)




