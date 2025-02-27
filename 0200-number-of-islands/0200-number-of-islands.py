class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        visited = set()

        def bfs(r,c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))

            while queue:
                row,coln = queue.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dx,dy in directions:
                    r=row+dx
                    c=coln+dy
                    if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    island+=1
        return island

        

        