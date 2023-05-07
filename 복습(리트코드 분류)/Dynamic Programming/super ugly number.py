import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = [1]
        cnt = 0

        done = set()
        while q:
            nxt = heapq.heappop(q)
            while nxt in done:
                nxt = heapq.heappop(q)
            done.add(nxt)
            cnt += 1
            if cnt == n: return nxt
            for i in primes:
                heapq.heappush(q, nxt*i)

# 다른 사람의 풀이
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = primes.copy() # do a deep copy 
        heapq.heapify(nums) #create a heap
        p = 1
        for i in range(n - 1):
            p = heapq.heappop(nums) #take the smallest element
            for prime in primes:
                heapq.heappush(nums, p * prime) #add all those multiples with the smallest number
                if p % prime == 0:
                    break
        return p