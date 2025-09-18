class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.d={}
        self.h=[]
        for i in range(len(tasks)):
            self.d[tasks[i][1]]=(tasks[i][2],tasks[i][0])
            heapq.heappush(self.h,(-tasks[i][-1],-tasks[i][1],tasks[i][0]))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.d[taskId] = ((priority,userId))
        heapq.heappush(self.h,(-priority,-taskId,userId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        u=self.d[taskId][1]
        self.d[taskId] =(newPriority,u)
        heapq.heappush(self.h,(-newPriority,-taskId,u))
        

    def rmv(self, taskId: int) -> None:
        del self.d[taskId]
        

    def execTop(self) -> int:
        while self.h:
            npriority,ntaskId,userId=heapq.heappop(self.h)
            p,t=-npriority,-ntaskId

            if t in self.d and self.d[t]==(p,userId):
                del self.d[t]
                return userId
        return -1
# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()