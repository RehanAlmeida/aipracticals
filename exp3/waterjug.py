def dfs_water_jug_problem(jug1_capacity, jug2_capacity, target):
    # To keep track of visited states to avoid revisiting
    visited_states = set() 
    # To store the sequence of actions leading to the solution 
    path = []
    # To count the number of steps  
    steps = -1  

    def dfs(jug1, jug2):
        # it is defined non local because it is not local to dfs , it is defined outer scope but it will  allow dfs to modify the seps
        
        nonlocal steps
        
        #check the base condition if either of one is equal to target
        if jug1 == target or jug2 == target:
            return True 

        # Try all possible actions: fill, empty, or transfer water between jugs
        actions = [('fill', 'jug1'), ('fill', 'jug2'), ('empty', 'jug1'), ('empty', 'jug2'), ('transfer', 'jug1', 'jug2'), ('transfer', 'jug2', 'jug1')]
        for action in actions:

            #initialise the new_state variable it will store result after applying the action
            new_state = None

            #Based on the type of action ('fill', 'empty', or 'transfer') and the jug(s) involved, calculates the new state resulting from the action.

            if action[0] == 'fill':
                new_state = (jug1_capacity, jug2) if action[1] == 'jug1' else (jug1, jug2_capacity)
            elif action[0] == 'empty':
                new_state = (0, jug2) if action[1] == 'jug1' else (jug1, 0)
            elif action[0] == 'transfer':
                if action[1] == 'jug1':
                    amount_to_transfer = min(jug1, jug2_capacity - jug2)
                    new_state = (jug1 - amount_to_transfer, jug2 + amount_to_transfer)
                else:
                    amount_to_transfer = min(jug2, jug1_capacity - jug1)
                    new_state = (jug1 + amount_to_transfer, jug2 - amount_to_transfer)


            # keep on checking if that state is there in visited states, if not add 
            if new_state not in visited_states:
                visited_states.add(new_state)

                #update the path also
                path.append((action, new_state))
                
                steps += 1  

                # recursively call dfs with the new state, if solution is found return true
                if dfs(*new_state):
                    return True  
                
                # pop the path and return false meaning no solution is found
                path.pop()  
        return False  

    # Start DFS from the initial state with both jugs empty
    dfs(0, 0)

    return path, steps

# Example usage:
jug1_capacity = int(input("enter the capacity for Jug1:"))
jug2_capacity = int(input("enter the capacity for Jug2:"))
target = int(input("enter the Target Capacity:"))
solution_path, num_steps = dfs_water_jug_problem(jug1_capacity, jug2_capacity, target)
for action, new_state in solution_path:
    print(action, new_state)
print("Number of steps:", num_steps)
