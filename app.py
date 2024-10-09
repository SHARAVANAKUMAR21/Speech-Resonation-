import streamlit as st
from speech_to_text import speech_to_text
from phoneme_comparison import phoneme_compare

# Title of the application
st.title("Pronunciation Assessment System")

# Input for correct sentence
correct_sentence = st.text_input("Enter the correct sentence:", "This is India")

# Button to start speech recognition
if correct_sentence.strip() == "":
    st.error("Please enter a valid correct sentence.")
else:
    if st.button("Start Speaking"):
        with st.spinner('Listening...'):
            spoken_text = speech_to_text()
            st.write(f"You said: {spoken_text}")
            
            # Compare spoken text with the correct sentence
            is_correct, feedback = phoneme_compare(spoken_text, correct_sentence)
            
            if is_correct:
                st.success("Pronunciation is correct! 🎉")
            else:
                st.error("Pronunciation needs improvement. ❌")
                
            st.write(feedback)
