from collections import deque

class GridProblem:
    def __init__(self,initial_state,goal_state,grid):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.grid = grid
        
    def is_goal(self,state):
        return state == self.goal_state
    
    def is_valid_cell(self,row,col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]) and self.grid[row][col] == 0
    
    def expand(self,node):
        row,col = node.state
        children = []
        
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            new_row,new_col = row + dr,col + dc
            if self.is_valid_cell(new_row,new_col):
                child_state = (new_row,new_col)
                child_node = Node(child_state,parent = node)
                children.append(child_node)
            
        return children

class Node :
    def __init__(self,state,parent = None,action = None):
        self.state = state
        self.parent = parent
        self.action = action
        
def breadth_first_search(problem):
    node = Node(problem.initial_state)
    if problem.is_goal(node.state):
        return node
    
    frontier = deque([node])
    reached = {problem.initial_state}
    
    while frontier:
        node = frontier.popleft()
        
        for child in problem.expand(node):
            state = child.state
            
            if problem.is_goal(state):
                return child
            
            if state not in reached:
                frontier.append(child)
                reached.add(state)
    
    return None

def reconstruct_path(node):
    path = []
    
    while node:
        path.append(node.state)
        node = node.parent
        
    return list(reversed(path))


def print_complete_path(path):
    # Prints the complete path from start to goal
    if path:
        for step, point in enumerate(path):
            print("Step {}: {}".format(step, point))
    else:
        print("No solution found")
        
"""
    1 : Denotes the obstacles
    0 : Empty space or a non-obstacle cell in the grid
"""
grid = [
    [0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0]
]

initial_state = (0,0)
goal_state = (0,6)

problem = GridProblem(initial_state,goal_state,grid)

solution_node = breadth_first_search(problem)

print('!! Reached the Goal!!' if solution_node else None)
if solution_node:
    print("Solution found!")
    solution_path = reconstruct_path(solution_node)
    print("Complete Path:")
    print_complete_path(solution_path)
else:
    print("No solution found")



