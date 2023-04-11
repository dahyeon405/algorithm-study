# 열심히 풀어봤으나 시간 초과
from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksq = []
        tasksCnt = dict(Counter(tasks))
        for key, val in tasksCnt.items():
            heapq.heappush(tasksq, (-val, key))
        
        waitTaskq = deque([])
        total = 0
        while len(tasksq) > 0:
            if len(waitTaskq) > n and len(waitTaskq) != 0: waitTaskq.popleft()
            popped = []
            isFound = False
            while len(tasksq) > 0:
                cnt, task = heapq.heappop(tasksq)
                cnt = -cnt
                if task not in waitTaskq:
                    if cnt > 1: heapq.heappush(tasksq, (-(cnt-1), task))
                    waitTaskq.append(task)
                    isFound = True
                    break
                else: popped.append((-cnt, task))
            total += 1
            if isFound is False: waitTaskq.append("idle")
            for el in popped:
                heapq.heappush(tasksq, el)

        return total

# 그냥 간단한 수학적 풀이..
def leastInterval(self, tasks, N):
    task_counts = collections.Counter(tasks).values()
    M = max(task_counts)
    Mct = task_counts.count(M)
    return max(len(tasks), (M - 1) * (N + 1) + Mct)