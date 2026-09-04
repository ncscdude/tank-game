import streamlit as st
from game_logic import check_hit
from obstacles import get_next_obstacle
from display import show_start, show_round, show_result, show_stats
from file_handler import save_game, load_history

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

    if st.session_state.player_name == "":
        st.session_state.player_name = st.text_input("Enter your name:")

    if st.session_state.player_name and st.session_state.round <= 5:
        st.write(f"Round {st.session_state.round} of 5")

        obstacle = get_next_obstacle(st.session_state.used_obstacles)
        st.session_state.used_obstacles.append(obstacle)

        wind = st.slider("Wind:", -10, 10, 0)
        angle = st.slider("Angle:", 0, 90, 45)
        velocity = st.slider("Velocity:", 1, 100, 50)

        st.write(f"Obstacle: {obstacle}")
        st.write("🎯 Target at 100 units | 🏹 Tank at 0 units")
        st.write(f"Wind: {wind} m/s {'→' if wind > 0 else '←'}")

        if st.button("Shoot!"):
            hit = check_hit(angle, velocity, wind)
            if hit:
                st.session_state.hits += 1
                st.success("Hit!")
            else:
                st.error("Miss!")
            st.session_state.round += 1
            st.rerun()

    elif st.session_state.player_name and st.session_state.round > 5:
        accuracy = (st.session_state.hits / 5) * 100
        save_game(st.session_state.player_name, st.session_state.hits, accuracy)
        st.write("=== GAME OVER ===")
        st.write(f"Player: {st.session_state.player_name}")
        st.write(f"Hits: {st.session_state.hits}/5")
        st.write(f"Accuracy: {accuracy:.1f}%")

        if st.button("Play Again"):
            st.session_state.round = 1
            st.session_state.hits = 0
            st.session_state.used_obstacles = []
            st.rerun()

if __name__ == "__main__":
    app()