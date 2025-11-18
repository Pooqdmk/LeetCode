class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.t = {}
        self.time = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.t[tokenId] =  currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.t:
            time = self.t[tokenId]
            if currentTime - time < self.time:
                self.t[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for k,v in self.t.items():
            if currentTime - v < self.time:
                cnt+=1
        return cnt



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)