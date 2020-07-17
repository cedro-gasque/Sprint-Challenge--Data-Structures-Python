class RingBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity

    def append(self, item):
        node = {'value': item, 'age': self.capacity}
        if len(self.buffer) == self.capacity:
            for i in range(self.capacity):
                if self.buffer[i]['age'] <= 0:
                    self.buffer[i] = node
                else:
                    self.buffer[i]['age'] -= 1
        else:
            for i in range(self.capacity):
                self.buffer[i]['age'] -= 1
            self.buffer.append(node)
    def get(self):
        return [node['value'] for node in self.buffer]
