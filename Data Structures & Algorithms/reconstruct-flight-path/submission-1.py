class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        
        # Sort tickets in reverse order so the smallest lexical destination 
        # is at the end of the list (enabling O(1) .pop())
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
            
        res = []
        
        def dfs(curr):
            # Visit all outgoing edges
            while adj[curr]:
                next_dest = adj[curr].pop()
                dfs(next_dest)
            # Post-order traversal: append to result after exhausting edges
            res.append(curr)
            
        dfs("JFK")
        
        # Reverse because post-order DFS builds the path from end to start
        return res[::-1]