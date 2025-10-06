import random

def calculate_attacks(board):
    """Calculates the number of attacking queen pairs (the heuristic)."""
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Check for diagonal attacks
            if abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_neighbors(board):
    """Generates all neighbor states by swapping two queens."""
    neighbors = []
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            neighbor = list(board)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(tuple(neighbor))
    return neighbors

def hill_climbing(initial_board):
    """Performs the hill-climbing search to find a solution."""
    current_board = initial_board
    current_attacks = calculate_attacks(current_board)

    while True:
        neighbors = get_neighbors(current_board)
        if not neighbors:
            break

        # Find the neighbor with the fewest attacks
        best_neighbor = min(neighbors, key=lambda b: calculate_attacks(b))
        best_neighbor_attacks = calculate_attacks(best_neighbor)

        # If no neighbor is better, we've reached a peak
        if best_neighbor_attacks >= current_attacks:
            return current_board, current_attacks
        
        # Move to the better state
        current_board = best_neighbor
        current_attacks = best_neighbor_attacks

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
    N = 8  # Board size (e.g., 8 for 8-Queens)

    # Generate a random initial state
    initial_board = tuple(random.sample(range(N), N))

    print("Initial Board (Attacks: {})".format(calculate_attacks(initial_board)))
    print_board(initial_board)
    print("-" * 20)

    # Run the algorithm
    solution, attacks = hill_climbing(initial_board)

    print("Final Solution (Attacks: {})".format(attacks))
    print_board(solution)
    
    if attacks == 0:
        print("\n✅ Found a solution!")
    else:
        print("\n⚠️ Stuck in a local minimum. Try running again.")