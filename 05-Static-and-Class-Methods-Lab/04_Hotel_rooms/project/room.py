class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests=0
        self.is_taken=False

    def take_room(self, people):
        if self.is_taken or people>self.capacity:
            return f"Room number {self.number} cannot be taken"
        self.guests=people
        self.is_taken=True

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.guests=0
        self.is_taken=False


