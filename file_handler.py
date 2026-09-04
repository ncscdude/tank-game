import csv
import os

def save_game(player_name, hits, accuracy):
    filename = "game_history.csv"
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Player", "Hits", "Accuracy"])
        writer.writerow([player_name, hits, f"{accuracy:.1f}"])

def load_history():
    filename = "game_history.csv"
    if not os.path.exists(filename):
        return []

    history = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            history.append(row)
    return history