# Tank Artillery Game - Project Plan

## Framework Complete
- game_state.py ✓
- obstacles.py (skeleton only)
- game_logic.py (skeleton only)
- file_handler.py (skeleton only)
- display.py ✓
- main.py (not started)

## Current Code Status

### game_state.py (COMPLETE)
```python
game_state = {
    "player_name": "",
    "round": 1,
    "hits": 0,
    "obstacles": [],
    "current_wind": 1
}
```

### display.py (COMPLETE - Skeletons)
```python
def show_start():
    pass

def show_round(round_num, wind, obstacle):
    pass

def show_result(hit_or_miss):
    pass

def show_stats(hits, accuracy, commentary):
    pass
```

### obstacles.py (SKELETON - needs logic)
```python
def generate_obstacles():
    pass

def get_next_obstacle(used_list):
    pass
```

### file_handler.py (NOT STARTED - needs skeleton)
Should have:
- load_history()
- save_game(player_name, hits, accuracy)

### game_logic.py (NOT STARTED - needs skeleton)
Should have:
- check_hit(angle, velocity, wind)

### main.py (NOT STARTED - needs main() orchestration)

## Next Steps (for tomorrow)
1. Complete file_handler.py skeleton
2. Complete game_logic.py skeleton
3. Complete main.py skeleton
4. Fill in display.py with actual print/input logic
5. Fill in file_handler.py with CSV/JSON logic
6. Fill in game_logic.py with ballistics math
7. Fill in obstacles.py with random generation
8. Test main.py integration

## Design Decisions Made
- Single player vs random obstacles (5-10)
- 5 rounds max per game
- Wind randomly assigned per round
- Hit detection: ±5 units tolerance
- 1D ballistics (distance only, not 2D physics)
- CSV for history, JSON for current state
- No graphics—terminal/DOS only

## Core Functions Table
| File | Function | Input | Output |
|------|----------|-------|--------|
| obstacles.py | generate_obstacles() | none | list of obstacles |
| obstacles.py | get_next_obstacle(used_list) | list | one obstacle |
| game_logic.py | check_hit(angle, velocity, wind) | 3 numbers | True/False |
| file_handler.py | load_history() | none | display CSV |
| file_handler.py | save_game(player_name, hits, accuracy) | 3 items | none |
| display.py | show_start() | none | player name |
| display.py | show_round(round_num, wind, obstacle) | 3 items | angle, velocity |
| display.py | show_result(hit_or_miss) | bool | message |
| display.py | show_stats(hits, accuracy, commentary) | 3 items | display |
| main.py | main() | none | orchestrate |