class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        self.buffer.extend(a)
        while len(self.buffer) >= 5:
            sum_of_five = sum(self.buffer[:5])
            print(sum_of_five)
            self.buffer = self.buffer[5:]

    def get_current_part(self):
        return self.buffer

buf = Buffer()

buf.add(1, 2, 3)
print(buf.get_current_part())  
buf.add(4, 5, 6)
print(buf.get_current_part())  
buf.add(7, 8, 9, 10)
print(buf.get_current_part())  
buf.add(11, 12)
print(buf.get_current_part())  
