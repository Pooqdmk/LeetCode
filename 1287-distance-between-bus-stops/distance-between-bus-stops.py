class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, end: int) -> int:
        if start>end:
            start,end=end,start

        x=sum(distance[start:end])

        return min(x,sum(distance)-x)