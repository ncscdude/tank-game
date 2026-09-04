def show_start():
    print("Welcome to the Tank Game!")
    print("Destroy the target in 5 rounds.")

def show_round(round_num, wind, obstacle):
    print(f"\nRound {round_num}:")
    print(f"Wind: {wind} m/s")
    print(f"Obstacle: {obstacle}")

def show_result(result):
    print(f"Result: {result}")

def show_stats(player_name, hits, accuracy):
    print(f"\n=== Game Over ===")
    print(f"Player: {player_name}")
    print(f"Hits: {hits}/5")
    print(f"Accuracy: {accuracy}%")
