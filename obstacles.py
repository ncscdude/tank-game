import random

def generate_obstacles():
    all_obstacles = ["hill", "valley", "wall", "bridge", "tunnel"]
    return all_obstacles

def get_next_obstacle(used_list):
    available = []
    for obstacle in generate_obstacles():
        if obstacle not in used_list:
            available.append(obstacle)
    return random.choice(available)
