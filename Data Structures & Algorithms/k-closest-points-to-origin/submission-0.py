class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res  = []

        for i, point in enumerate(points):
            distance = math.sqrt(((point[0] - 0) ** 2) + ((point[1] - 0) ** 2))
            heapq.heappush(minHeap,[distance, i])
        
        for i in range(k):
            closest = heapq.heappop(minHeap)
            res.append(points[closest[1]])
        return res