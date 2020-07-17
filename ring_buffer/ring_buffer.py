class RingBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.age = []
        self.capacity = capacity

    def append(self, item):
        if len(self.buffer) >= self.capacity:
            for i in range(self.capacity):
                if self.age[i] <= 0:
                    self.buffer[i] = item
                    self.age[i] = self.capacity - 1
                else:
                    self.age[i] -= 1
        else:
            for i in range(len(self.age)):
                self.age[i] -= 1
            self.buffer.append(item)
            self.age.append(self.capacity - 1)
        print(self.buffer)
    def get(self):
        return self.buffer

if __name__ == "__main__":
    ring = RingBuffer(5)
    ring.append(1)
    ring.append(2)
    ring.append(3)
    ring.append(4)
    ring.append(5)
    ring.append(6)
