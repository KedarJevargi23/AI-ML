import random
import math

def calculate_attacks(board):
    """Calculates the number of attacking queen pairs."""
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def simulated_annealing(initial_board):
    """Performs the simulated annealing search."""
    # Hyperparameters
    temp = 100
    stopping_temp = 0.0001
    alpha = 0.999 # Cooling rate

    current_board = list(initial_board)
    current_attacks = calculate_attacks(current_board)
    
    best_board = list(current_board)
    best_attacks = current_attacks

    while temp > stopping_temp:
        # Get a random neighbor by moving one queen to a new row
        neighbor = list(current_board)
        n = len(neighbor)
        col_to_move = random.randint(0, n - 1)
        new_row = random.randint(0, n - 1)
        neighbor[col_to_move] = new_row
        
        neighbor_attacks = calculate_attacks(neighbor)
        
        # Calculate the change in "energy" (cost)
        delta = neighbor_attacks - current_attacks
        
        # If the new solution is better, always accept it
        if delta < 0:
            current_board = list(neighbor)
            current_attacks = neighbor_attacks
            # Check if this is the best solution found so far
            if current_attacks < best_attacks:
                best_board = list(current_board)
                best_attacks = current_attacks
        # If the new solution is worse, accept it with a certain probability
        else:
            acceptance_prob = math.exp(-delta / temp)
            if random.random() < acceptance_prob:
                current_board = list(neighbor)
                current_attacks = neighbor_attacks
        
        # Cool the temperature
        temp *= alpha
        
    return best_board, best_attacks

def print_board(board):
    """A helper function to print the board nicely."""
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)

# --- Main Execution ---
if __name__ == "__main__":
    N = 8  # Board size

    # Generate a random initial state
    initial_board = [random.randint(0, N - 1) for _ in range(N)]

    print("Initial Board (Attacks: {})".format(calculate_attacks(initial_board)))
    print_board(initial_board)
    print("-" * 20)

    solution, attacks = simulated_annealing(initial_board)

    print("Final Solution (Attacks: {})".format(attacks))
    print_board(solution)
    
    if attacks == 0:
        print("\n✅ Found a global optimum (solution)!")
    else:
        print("\n⚠️ May be stuck in a local minimum. Try different parameters or run again.")