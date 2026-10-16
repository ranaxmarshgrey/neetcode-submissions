class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])

        visit=set()

        islands=0
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    next_row, next_col = row + dr, col + dc
                    
                    if (next_row in range(rows) and 
                        next_col in range(cols) and
                        grid[next_row][next_col] == "1" and
                        (next_row, next_col) not in visit):
                        
                        q.append((next_row, next_col))
                        visit.add((next_row, next_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands