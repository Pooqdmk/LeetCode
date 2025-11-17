class BrowserHistory:

    def __init__(self, homepage: str):
        self.a = [homepage]
        self.c = 0
    def visit(self, url: str) -> None:
        self.a = self.a[:self.c+1]
        self.a.append(url)
        self.c+=1
        
    def back(self, steps: int) -> str:
        self.c = max(0,self.c-steps)
        return self.a[self.c]
    def forward(self, steps: int) -> str:
        self.c = min(len(self.a)-1, self.c+steps)
        return self.a[self.c]
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)