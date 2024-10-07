from speech_to_text import speech_to_text
from phoneme_comparison import compare_sentence_phonemes

def real_time_feedback(correct_sentence):
    spoken_text = speech_to_text()
    if spoken_text:
        compare_sentence_phonemes(spoken_text, correct_sentence)

if __name__ == "__main__":
    correct_sentence = "This is India"
    real_time_feedback(correct_sentence)
