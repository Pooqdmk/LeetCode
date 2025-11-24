class Skiplist:

    def __init__(self):
        self.a = []
        self.seen = set()

    def search(self, target: int) -> bool:
        if target in self.seen:
            return True
        return False

    def add(self, num: int) -> None:
        self.a.append(num)
        self.seen.add(num)

    def erase(self, num: int) -> bool:
        if num in self.seen:
            self.a.remove(num)
            if num not in self.a:
                self.seen.remove(num)
            return True
        return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)