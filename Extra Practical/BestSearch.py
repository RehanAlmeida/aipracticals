import heapq
import random


def heuristic(state):
    left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat_position = state
    return left_missionaries + left_cannibals  


def get_possible_moves(state):
    left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat_position = state
    possible_moves = []

    
    transitions = [
        (1, 0),  
        (2, 0),  
        (0, 1),  
        (0, 2),  
        (1, 1),  
    ]

    
    for transition in transitions:
        m, c = transition  
        if boat_position == 'left':
            new_left_m = left_missionaries - m
            new_left_c = left_cannibals - c
            new_right_m = right_missionaries + m
            new_right_c = right_cannibals + c
            new_boat_position = 'right'
        else:
            new_left_m = left_missionaries + m
            new_left_c = left_cannibals + c
            new_right_m = right_missionaries - m
            new_right_c = right_cannibals - c
            new_boat_position = 'left'

        
        if (
            new_left_m >= 0
            and new_left_c >= 0
            and new_right_m >= 0
            and new_right_c >= 0
            and (new_left_m == 0 or new_left_m >= new_left_c)
            and (new_right_m == 0 or new_right_m >= new_right_c)
        ):
            possible_moves.append(
                (
                    new_left_m,
                    new_left_c,
                    new_right_m,
                    new_right_c,
                    new_boat_position,
                )
            )

    return possible_moves


def gbfs(start, goal):
    
    queue = []
    heapq.heappush(queue, (heuristic(start), start, []))  

    visited = set()  

    while queue:
        _, current_state, path = heapq.heappop(queue)

        if current_state == goal:
            return path  
        if current_state not in visited:
            visited.add(current_state)

            
            for new_state in get_possible_moves(current_state):
                if new_state not in visited:
                    new_path = path + [new_state]
                    heapq.heappush(queue, (heuristic(new_state), new_state, new_path))

    return None  


if __name__ == "__main__":
    
    start_state = (3, 3, 0, 0, 'left')
    
    goal_state = (0, 0, 3, 3, 'right')

   
    solution = gbfs(start_state, goal_state)

    if solution:
        print("Greedy Best-First Search Solution:")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")

#Output:  Rehan Almeida 9586 Greedy Best-First Search of Missionaries and Cannibals Solution:
#Step I: (3, 3, 0, 0, 'left')
#Step 0: (2, 2, 1, 1, 'right')
#Step 1: (3, 2, 0, 1, 'left')
#Step 2: (3, 0, 0, 3, 'right')
#Step 3: (3, 1, 0, 2, 'left')
#Step 4: (1, 1, 2, 2, 'right')
#Step 5: (2, 2, 1, 1, 'left')
#Step 6: (0, 2, 3, 1, 'right')
#Step 7: (0, 3, 3, 0, 'left')
#Step 8: (0, 1, 3, 2, 'right')
#Step 9: (0, 2, 3, 1, 'left')
#Step 10: (0, 0, 3, 3, 'right')
