import random

def generate_obstacles():
    all_obstacles = ["hill", "valley", "wall", "bridge", "tunnel"]
    return all_obstacles

def get_next_obstacle(used_list):
    all_obstacles = generate_obstacles()
    available = [obs for obs in all_obstacles if obs not in used_list]
    if available:
        return random.choice(available)
    else:
        return random.choice(all_obstacles)