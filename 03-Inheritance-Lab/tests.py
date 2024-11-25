class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print(f"Counters created: {cls.count}")
        return two_counters
Counter.create_two()