import sys
class Node():
    def __init__(self,parent,state,action):
        self.parent = parent
        self.state = state
        self.action = action
class StackFrontier():
    def __init__(self):
        self.frontier = []
    def add(self,node):
        self.frontier.append(node)
    def contains_state(self,state):
        return any(node.state == state for node in self.frontier)
    def empty(self):
        return len(self.frontier) == 0
    def remove(self):
        if(self.empty()):
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
class QueueFrontier(StackFrontier):
    def remove(self):
        if (self.empty()):
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Maze():
    def __init__(self,filename):
        with open(filename) as f:
            contents = f.read()
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")
        contents = contents.splitlines(contents)
        self.height = len(contents)
        self.width = max(len(line) for line in contents)
        self.wall = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i,j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        self.solution = None

        def print(self):


        def neighbors(self,state):
            row, col = state
            candidates = {
                ("up",(row+1,col)),
                ("down",(row-1,col)),
                ("left",(row,col-1)),
                ("right",(row,col+1))
            }
            result = []
            for action,(r,c) in candidates:
                if 0<=r<self.height and 0<=c<self.width and not self.wall[r][c]:
                    result.append((action,(r,c)))
            return result



        def solve(self):
            self.num_explored = 0
            start = Node(state=self.start,parent = None,action=None)
            frontier = StackFrontier()
            frontier.add(start)
            self.num_explored = set()
            while True:
                if frontier.empty():
                    raise Exception("no solution")
                node = frontier.remove()
                self.num_explored += 1
                if node.state == self.goal:
                    actions = []
                    cells = []
                    while node.parent is not None:
                        actions.append(node.action)
                        cells.append(node.state)
                        node = node.parent
                    actions.reverse()
                    cells.reverse()
                    self.solution(actions,cells)
                    return
                self.explored.add(node.state)
                for action,state in self.neighbors(node.state)




