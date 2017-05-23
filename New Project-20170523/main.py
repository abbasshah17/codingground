from collections import deque

class Node:

    def __init__(self, x, y, jump, grid):
        self.x = x
        self.y = y;
        self.jump = jump
        self.grid = grid

    def __hash__(self):
        return hash((self.x, self.y, self.jump))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.jump == other.jump

    def getNeighbors(self):
        neighbors = []
        x = self.x
        y = self.y
        jump = self.jump
        grid = self.grid
        rows = len(grid)
        columns = len(grid[0])

        if x > 0:
            wall = grid[y][x - 1] == 1
            if wall:
                if jump > 0:
                    neighbors.append(Node(x - 1, y, jump - 1, grid))
            else:
                neighbors.append(Node(x - 1, y, jump, grid))

        if x < columns - 1:
            wall = grid[y][x + 1] == 1
            if wall:
                if jump > 0:
                    neighbors.append(Node(x + 1, y, jump - 1, grid))
            else:
                neighbors.append(Node(x + 1, y, jump, grid))

        if y > 0:
            wall = grid[y - 1][x] == 1
            if wall:
                if jump > 0:
                    neighbors.append(Node(x, y - 1, jump - 1, grid))
            else:
                neighbors.append(Node(x, y - 1, jump, grid))

        if y < rows - 1:
            wall = grid[y + 1][x]
            if wall:
                if jump > 0:
                    neighbors.append(Node(x, y + 1, jump - 1, grid))
            else:
                neighbors.append(Node(x, y + 1, jump, grid))

        return neighbors


class MazeBreaker:

    def __init__(self, grid, jump):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.jump = jump

    def getShortestPath(self):
        source = Node(0, 0, self.jump, self.grid)
        queue = deque([source])
        steps = {source: 1}

        while queue:
            currentNode = queue.popleft()

            if currentNode.x == self.columns - 1 and currentNode.y == self.rows - 1:
                return steps[currentNode]

            for neighbor in currentNode.getNeighbors():
                if neighbor not in steps.keys():
                    steps[neighbor] = steps[currentNode] + 1
                    queue.append(neighbor)

        return 0
    
def answer(map):
    
    if len(map) < 2 or len(map[0]) < 2 or len(map) > 20 or len(map[0]) > 20:
        return 0

    breaker = MazeBreaker(map, 1)
    return breaker.getShortestPath()

print "Result ", answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])