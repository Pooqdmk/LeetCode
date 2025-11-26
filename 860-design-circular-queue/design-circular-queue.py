class MyCircularQueue:

    def __init__(self, k: int):
        self.a = []
        self.k = k
    def enQueue(self, value: int) -> bool:
        if len(self.a) < self.k:
            self.a.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if self.a:
            self.a = self.a[1:]
            return True
        return False

    def Front(self) -> int:
        return self.a[0] if self.a else -1

    def Rear(self) -> int:
        return self.a[-1] if self.a else -1

    def isEmpty(self) -> bool:
        return len(self.a) < 1


    def isFull(self) -> bool:
        return len(self.a) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()