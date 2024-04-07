# implementing constraints of Missionaries & cannibal problem
def is_valid(left_m, left_c, side ,right_m, right_c):
    # node which implies empty boat is invalid
    if left_m < 0 or left_c < 0 or right_m < 0 or right_c < 0:
        return False
    # node with cannibals outnumbering missionaries is invalid
    if (left_m > 0 and left_c > left_m) or (right_m > 0 and right_c > right_m):
        return False
    # rest nodes are acceptable
    return True

# goal state: all 3 cannibals and missionaries reach on right side
def is_goal(left_m, left_c, side , right_m , right_c):
    return left_m == 0 and left_c == 0

# iterate to next node
def get_next_states(current_state):
    # list to store states
    next_states = []
    left_m, left_c, boat, right_m, right_c = current_state
    # if boat is at left bank traverse towards right
    if boat == 'left':
        for m in range(3):
            for c in range(3):
                # at most 2 people on boat
                if 1 <= m + c <= 2:
                    # subtract from left bank add to right bank
                    new_state = (left_m - m, left_c - c, 'right', right_m + m, right_c + c)
                    # if valid add to new_states list
                    if is_valid(*new_state):
                        next_states.append(new_state)
    # if boat at right bank traverse towards left
    else:
        for m in range(3):
            for c in range(3):
                # at most 2 people on boat
                if 1 <= m + c <= 2:
                    # subtract from right bank add to left bank
                    new_state = (left_m + m, left_c + c, 'left', right_m - m, right_c - c)
                    # if valid add to new_states list
                    if is_valid(*new_state):
                        next_states.append(new_state)
    return next_states

def dfs_search(initial_state):
    # store all visited nodes
    visited = set()
    stack = [(initial_state, [])]
    # iterate until stack is empty
    while stack:
        # pop out current state and the path taken so far
        current_state, path = stack.pop()
        # if current state is goal state return final path
        if is_goal(*current_state):
            return path + [current_state]
        # if node is not a goal state has not been visited
        if current_state not in visited:
            # mark non visited current state as visited
            visited.add(current_state)
            # all possible next steps
            for next_state in get_next_states(current_state):
                # push unvisited next state on the stack along with the updated path
                if next_state not in visited:
                    stack.append((next_state, path + [current_state]))
    # if no solution found
    return False

def print_solution(solution):
    # iterate and print path
    print("Left Bank Right Bank")
    print("M C Side M C")
    if solution:
        for state in (solution):
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    initial_state = (3, 3, 'left', 0, 0)
    solution = dfs_search(initial_state)
    print_solution(solution)
