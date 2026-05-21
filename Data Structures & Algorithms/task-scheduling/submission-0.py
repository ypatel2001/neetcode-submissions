class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Big O of n * m (which is the n idletime)
        count  = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque() #pairs of [-cnt, idleTime]
        time = 0
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap) # we add 1 as we are using negative values so we need to decrement val by adding 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
               

