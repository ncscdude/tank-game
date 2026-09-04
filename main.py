import

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


