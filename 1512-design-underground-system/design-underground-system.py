class UndergroundSystem:

    def __init__(self):
        self.checkedIn = {}
        self.checkedOut = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedIn:
            self.checkedIn[id] = [stationName,t]


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkedIn:
            station,st=self.checkedIn[id]
            self.checkedOut[(station,stationName)].append(t-st)
            del self.checkedIn[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # if (startStation,endStation) in self.checkedOut:
        l = self.checkedOut[(startStation,endStation)]
        return sum(l)/len(l)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)