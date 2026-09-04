# Tank Game
Python 101 capstone project

A strategic tank artillery game built with Python and Streamlit. Destroy the target in 5 rounds by adjusting angle, velocity, and accounting for wind conditions.

## Features

- **5-Round Gameplay** — Each round presents a new random obstacle
- **Physics Simulation** — Bullets follow a calculated trajectory based on angle, velocity, and wind
- **Dynamic Obstacles** — Hill, valley, wall, bridge, tunnel (no repeats per game)
- **Wind System** — Wind affects bullet distance; direction shown as arrow
- **Scoring System** — Tracks hits/accuracy; results saved to CSV
- **CSV History** — All game results stored in `game_history.csv` for tracking progress

## How to Play

1. Enter your name
2. For each of 5 rounds:
   - Adjust **Angle** (0-90°)
   - Set **Velocity** (1-100 m/s)
   - Account for **Wind** (-10 to +10 m/s)
   - Click **Shoot!**
   - Bullet lands at calculated distance; compare to target (100 units)
3. See final accuracy after round 5
4. Play again to add to your history

## Game Physics
