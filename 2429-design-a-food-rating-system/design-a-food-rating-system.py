class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        self.d = defaultdict(SortedSet)
        self.l = {}
        self.r={}
        for i in range(len(foods)):
            self.d[cuisines[i]].add((-ratings[i],foods[i]))
            self.l[foods[i]] = cuisines[i]
            self.r[foods[i]] = -ratings[i]
        
        
            

    def changeRating(self, food: str, newRating: int) -> None:
        self.d[self.l[food]].remove((self.r[food],food))
        self.d[self.l[food]].add((-newRating,food))

        self.r[food] = -newRating

    def highestRated(self, cuisine: str) -> str:
        return self.d[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)