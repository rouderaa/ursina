class RoundRobinBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0  # Points to the next insertion point
        self.count = 0  # Keeps track of the number of elements in the buffer

    def push(self, item):
        # Overwrite the item at the current head position
        self.buffer[self.head] = item

        # Move the head pointer to the next position
        self.head = (self.head + 1) % self.size

        # If the buffer is full, maintain the size by not increasing the count further
        if self.count < self.size:
            self.count += 1

    def peek(self, offset=0):
        if self.is_empty() or offset >= self.count:
            return None

        # Calculate the index based on the head position and the offset
        index = (self.head - self.count + offset) % self.size
        return self.buffer[index]

    def is_empty(self):
        # The buffer is empty if the count is zero
        return self.count == 0

    def __len__(self):
        # The number of elements in the buffer is stored in `count`
        return self.count

    def __str__(self):
        return str(self.buffer)
