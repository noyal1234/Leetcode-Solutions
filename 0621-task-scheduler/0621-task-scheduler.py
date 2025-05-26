class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = Counter(tasks)
        heap = []
        for task,freq in task_freq.items():
            heapq.heappush(heap,-freq)
        time=0
        waitq = deque()
        while heap or waitq:
            time+=1
            if heap:
                curr_task = heapq.heappop(heap)
                curr_task+=1

                if curr_task != 0:
                    waitq.append((curr_task,time+n))
            if waitq and waitq[0][1] == time:
                heapq.heappush(heap,waitq.popleft()[0])
        return time

