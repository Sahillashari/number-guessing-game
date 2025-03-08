import streamlit as st
import random

def start_new_game():
    st.session_state['random_number'] = random.randint(st.session_state['min_range'], st.session_state['max_range'])
    st.session_state['attempts'] = 0
    st.session_state['game_over'] = False

def set_difficulty(level):
    difficulties = {'Easy': 10, 'Medium': 7, 'Hard': 5}
    st.session_state['max_attempts'] = difficulties[level]

def main():
    st.title("🎯 Number Guessing Game By Sahil Lashari")
    
    if 'min_range' not in st.session_state:
        st.session_state['min_range'] = 1
    if 'max_range' not in st.session_state:
        st.session_state['max_range'] = 100
    if 'random_number' not in st.session_state:
        st.session_state['random_number'] = random.randint(st.session_state['min_range'], st.session_state['max_range'])
    if 'attempts' not in st.session_state:
        st.session_state['attempts'] = 0
    if 'game_over' not in st.session_state:
        st.session_state['game_over'] = False
    if 'max_attempts' not in st.session_state:
        st.session_state['max_attempts'] = 10
    
    # Custom Range Selection
    with st.expander("⚙️ Set Custom Range"):
        min_range = st.number_input("Minimum Number", value=st.session_state['min_range'], step=1)
        max_range = st.number_input("Maximum Number", value=st.session_state['max_range'], step=1)
        if st.button("Apply Range"):
            st.session_state['min_range'] = min_range
            st.session_state['max_range'] = max_range
            start_new_game()
    
    # Difficulty Levels
    difficulty = st.selectbox("Select Difficulty Level", ["Easy", "Medium", "Hard"], index=0)
    set_difficulty(difficulty)
    
    # Number Input for Guessing
    guess = st.number_input("Enter Your Guess", min_value=st.session_state['min_range'], max_value=st.session_state['max_range'], step=1)
    if st.button("Submit Guess") and not st.session_state['game_over']:
        st.session_state['attempts'] += 1
        if guess < st.session_state['random_number']:
            st.warning("Too Low! Try Again 🔽")
        elif guess > st.session_state['random_number']:
            st.warning("Too High! Try Again 🔼")
        else:
            st.success(f"🎉 Correct! The number was {st.session_state['random_number']} in {st.session_state['attempts']} attempts.")
            st.session_state['game_over'] = True
        
        if st.session_state['attempts'] >= st.session_state['max_attempts'] and not st.session_state['game_over']:
            st.error(f"❌ Game Over! The correct number was {st.session_state['random_number']}")
            st.session_state['game_over'] = True
    
    st.write(f"Attempts: {st.session_state['attempts']}/{st.session_state['max_attempts']}")
    
    if st.button("🔄 Restart Game"):
        start_new_game()

if __name__ == "__main__":
    main()
