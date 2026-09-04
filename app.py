import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from game_logic import check_hit
from obstacles import get_next_obstacle
from file_handler import save_game
import matplotlib
matplotlib.use('Agg')

def draw_game_state(angle, velocity, wind, obstacle_type, impact_distance, target_hit):
    """Visualize the tank shot trajectory and impact."""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(-5, 120)
    ax.set_ylim(-5, 50)
    ax.set_aspect('equal')

    # Tank (green rectangle + barrel)
    tank = patches.Rectangle((0, 0), 3, 2, color='darkgreen', ec='black', lw=2)
    ax.add_patch(tank)
    barrel_x = [3, 3 + 4*np.cos(np.radians(angle))]
    barrel_y = [1, 1 + 4*np.sin(np.radians(angle))]
    ax.plot(barrel_x, barrel_y, 'darkgreen', lw=4, solid_capstyle='round')

    # Target (red circle at 100 units)
    target = patches.Circle((100, 0), 2.5, color='red', alpha=0.7, ec='darkred', lw=2)
    ax.add_patch(target)
    ax.text(100, -3.5, 'TARGET', ha='center', fontsize=10, weight='bold')

    # Obstacle
    obs_height_map = {'hill': 12, 'valley': -2, 'wall': 18, 'bridge': 8, 'tunnel': 3}
    obs_y = obs_height_map.get(obstacle_type, 10)
    obstacle = patches.Rectangle((45, obs_y-1.5), 10, 3, color='gray', ec='black', lw=2, alpha=0.6)
    ax.add_patch(obstacle)
    ax.text(50, obs_y+2, obstacle_type.upper(), ha='center', fontsize=9, style='italic')

    # Trajectory arc
    g = 9.81
    t_max = 2 * velocity * np.sin(np.radians(angle)) / g
    if t_max > 0:
        t_array = np.linspace(0, t_max, 150)
        x_traj = velocity * np.cos(np.radians(angle)) * t_array + wind * 0.5 * t_array
        y_traj = velocity * np.sin(np.radians(angle)) * t_array - 0.5 * g * t_array**2
        ax.plot(x_traj, y_traj, color='orange', lw=2.5, label='Trajectory', alpha=0.8)

    # Impact point marker
    if impact_distance is not None and impact_distance >= 0:
        ax.plot(impact_distance, 0, marker='*', color='yellow', markersize=20,
                markeredgecolor='orange', markeredgewidth=2, label='Impact', zorder=5)

        distance_off = abs(impact_distance - 100)
        if target_hit:
            ax.text(50, 42, 'HIT!', fontsize=18, ha='center', weight='bold',
                   color='green', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
        else:
            ax.text(50, 42, f'MISS: {distance_off:.1f}m off target', fontsize=14, ha='center',
                   color='orange', weight='bold', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # Wind indicator
    wind_arrow_len = abs(wind) * 1.5
    wind_direction = 1 if wind >= 0 else -1
    ax.arrow(10, 35, wind_arrow_len * wind_direction, 0, head_width=1.5, head_length=1.2,
            fc='blue', ec='blue', lw=2)
    ax.text(10, 38.5, f'Wind: {wind:+d} m/s', fontsize=11, weight='bold', color='blue')

    # Ground line
    ax.axhline(y=0, color='brown', linestyle='-', lw=3, alpha=0.5)

    ax.set_xlabel('Distance (meters)', fontsize=11, weight='bold')
    ax.set_ylabel('Height (meters)', fontsize=11, weight='bold')
    ax.set_title(f'Angle: {angle}° | Velocity: {velocity} m/s | Obstacle: {obstacle_type}',
                fontsize=13, weight='bold')
    ax.grid(True, alpha=0.2, linestyle='--')
    ax.legend(loc='upper left', fontsize=10)

    plt.tight_layout()
    return fig

def app():
    st.title("Tank Game")

    if "player_name" not in st.session_state:
        st.session_state.player_name = ""
    if "round" not in st.session_state:
        st.session_state.round = 1
    if "hits" not in st.session_state:
        st.session_state.hits = 0
    if "used_obstacles" not in st.session_state:
        st.session_state.used_obstacles = []
    if "current_obstacle" not in st.session_state:
        st.session_state.current_obstacle = None

    if st.session_state.player_name == "":
        st.session_state.player_name = st.text_input("Enter your name:")

    if st.session_state.player_name and st.session_state.round <= 5:
        st.write(f"**Round {st.session_state.round} of 5**")
        st.write("TANK ================ 100 units ================ TARGET")

        if st.session_state.current_obstacle is None:
            st.session_state.current_obstacle = get_next_obstacle(st.session_state.used_obstacles)

        obstacle = st.session_state.current_obstacle
        wind = st.slider("Wind:", -10, 10, 0)
        angle = st.slider("Angle:", 0, 90, 45)
        velocity = st.slider("Velocity:", 1, 100, 50)

        st.write(f"**Obstacle:** {obstacle} | **Wind:** {wind} m/s")

        if st.button("Shoot!"):
            hit = check_hit(angle, velocity, wind)
            distance = (velocity ** 2 * np.sin(2 * np.radians(angle)) / 9.81) + (wind * 2)

            fig = draw_game_state(angle, velocity, wind, obstacle, distance, hit)

            st.session_state.last_fig = fig
            st.session_state.last_distance = distance
            st.session_state.last_hit = hit

        if "last_fig" in st.session_state:
            st.pyplot(st.session_state.last_fig)
            st.write(f"Distance: {st.session_state.last_distance:.0f} units (Target: 100)")

            if st.session_state.last_hit:
                st.session_state.hits += 1
                st.success("Hit!")
            else:
                st.error("Miss!")

            if st.button("Next Round"):
                st.session_state.used_obstacles.append(obstacle)
                st.session_state.current_obstacle = None
                st.session_state.round += 1
                st.session_state.pop("last_fig", None)
                st.rerun()

    elif st.session_state.player_name and st.session_state.round > 5:
        accuracy = (st.session_state.hits / 5) * 100
        save_game(st.session_state.player_name, st.session_state.hits, accuracy)
        st.write(f"GAME OVER | {st.session_state.player_name} | Hits: {st.session_state.hits}/5 | Accuracy: {accuracy:.1f}%")

        if st.button("Play Again"):
            st.session_state.round = 1
            st.session_state.hits = 0
            st.session_state.used_obstacles = []
            st.rerun()

if __name__ == "__main__":
    app()