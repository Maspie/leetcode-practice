class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task = Counter(tasks)

        freq = [-x for x in task.values()]

        heapq.heapify(freq)

        q = deque()
        time = 0

        while q or freq:
            time += 1

            if freq:
                count = heapq.heappop(freq)
                #dec count for that counter
                count += 1 

                if count != 0:
                    q.append([count, time + n])

            
            if q and q[0][1] == time:

                count, time_ready = q.popleft()

                heapq.heappush(freq, count)

        return time






        