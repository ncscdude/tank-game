import random
from obstacles import get_next_obstacle
from game_logic import check_hit
from display import show_start, show_round, show_result, show_stats
from file_handler import save_game


def main():
    player_name = input("Enter your name: ")
    hits = 0
    rounds = 5
    for round_num in range(1, rounds + 1):
        obstacle = get_next_obstacle([])
        angle = int(input("Enter angle: "))
        velocity = int(input("Enter velocity: "))
        wind = random.randint(-10, 10)
        hit = check_hit(angle, velocity, wind)
        if hit:
            hits += 1
            show_result("Hit!")
        else:
            show_result("Miss!")
        show_round(round_num, wind, obstacle)

    accuracy = (hits / rounds) * 100
    save_game(player_name, hits, accuracy)
    show_stats(player_name, hits, accuracy)

if __name__ == "__main__":
    main()
