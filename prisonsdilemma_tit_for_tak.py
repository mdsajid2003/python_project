import numpy as np

# Number of rounds
rounds = 10

# Lists to store the moves and scores for each round
moves_player1 = []
moves_player2 = []
scores_player1 = []
scores_player2 = []

# Function to determine scores based on the moves
def get_scores(move1, move2):
    if move1 == 'silent' and move2 == 'silent':
        return 2, 2
    elif move1 == 'confess' and move2 == 'silent':
        return 1, 8
    elif move1 == 'silent' and move2 == 'confess':
        return 8, 1
    elif move1 == 'confess' and move2 == 'confess':
        return 5, 5

# --- Round 1 ---
# Both players start by cooperating (choosing "silent")
move1 = 'silent'
move2 = 'silent'
moves_player1.append(move1)
moves_player2.append(move2)
s1, s2 = get_scores(move1, move2)
scores_player1.append(s1)
scores_player2.append(s2)
print(f"Round 1: Player1: {move1}, Player2: {move2}")

# --- Rounds 2 to 10 ---
# In tit-for-tat, each player mimics the opponent's previous move.
for i in range(1, rounds):
    # Player 1 copies player 2's previous move
    move1 = moves_player2[i-1]
    # Player 2 copies player 1's previous move
    move2 = np.random.choice(['confess','silent'])
    
    moves_player1.append(move1)
    moves_player2.append(move2)
    
    s1, s2 = get_scores(move1, move2)
    scores_player1.append(s1)
    scores_player2.append(s2)
    
    print(f"Round {i+1}: Player1: {move1}, Player2: {move2}")

# --- Final Results ---
print("\nFinal moves and scores:")
print("Player 1 moves:", moves_player1)
print("Player 2 moves:", moves_player2)
print("Player 1 round scores:", scores_player1, "Total:", sum(scores_player1))
print("Player 2 round scores:", scores_player2, "Total:", sum(scores_player2))
