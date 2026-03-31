class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []
        for num in nums:
            if num in count:
                count[num]+=1
            else: count[num] = 1
        maxCount = max(list(count.values()))
        bucket = [[] for _ in range(maxCount+1)] 
        arr = list(count.items())
        for [key,value] in arr:
            bucket[value].append(key)
        for arr in reversed(bucket):
            if len(arr) > 0:
                if len(output) < k:
                    output.extend(arr)
                else: 
                    print(output)
                    return output
            else:
                if len(output) == k:
                    return output

        print(bucket)
        
            