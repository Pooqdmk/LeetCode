class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented = defaultdict(SortedSet)
        self.rented=SortedSet()
        self.price_list={}
        for i,j,k in entries: #(shop,movie,price)
            self.unrented[j].add((k,i)) #movie:(price,shop)
            self.price_list[(i,j)] = k


    def search(self, movie: int) -> List[int]:
        l = self.unrented[movie]
        keys=5
        res=[]
        for i in l:
            if keys > 0:
                res.append(i[-1])
                keys-=1
            else:
                break
        return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_list[(shop,movie)]
        self.rented.add((price,shop,movie))
        self.unrented[movie].remove((price,shop))
    def drop(self, shop: int, movie: int) -> None:
        
        price = self.price_list[(shop,movie)]
        self.rented.remove((price,shop,movie))
        self.unrented[movie].add((price,shop))
        

    def report(self) -> List[List[int]]:
        res=[]
        k=5
        for i in self.rented:
            if k>0:
                res.append([i[1],i[-1]])
                k-=1
            else:
                break
        return res

        
# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()