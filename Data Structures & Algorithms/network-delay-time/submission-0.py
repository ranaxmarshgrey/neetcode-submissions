class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={i:[] for i in range(1,n+1)}
        for time in times:
            graph[time[0]].append((time[1],time[2]))

        dist=[float('inf')]*(n+1)
        dist[k]=0
        min_heap=[]
        heapq.heappush(min_heap,(0,k))

        while min_heap:
            at,node=heapq.heappop(min_heap) 
            if at>dist[node]:
                continue
            for neighbor,weight in graph[node]:
                new_time=at+weight
                if new_time<dist[neighbor]:
                    dist[neighbor]=new_time
                    heapq.heappush(min_heap,(new_time,neighbor))
            
        for i in range(1,len(dist)+1):
            if i<n+1 and dist[i]==float('inf'):
                return -1
        return max(dist[1:])




        
        