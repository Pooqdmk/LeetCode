class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        a = [i for i in range(n)]
        used = []  #(end, room)
        count = [0]*n

        for start,end in meetings:

            while used and start >= used[0][0]:
                _,room = heapq.heappop(used)
                heapq.heappush(a,room)
            
            if not a:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)

                heapq.heappush(a,room)
            
            room = heapq.heappop(a)
            heapq.heappush(used, (end,room))

            count[room]+=1
        return count.index(max(count))