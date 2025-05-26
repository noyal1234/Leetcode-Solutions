class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        darr = []
        for point in points:
            x,y = point
            distance = -( x*x + y*y )
            if len(darr) == k:
                heapq.heappushpop(darr,(distance,x,y))
            else:
                heapq.heappush(darr,(distance,x,y))

        return [(x,y) for (distance,x,y) in darr]
