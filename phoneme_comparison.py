def phoneme_compare(spoken_text, correct_sentence):
    # Simple comparison logic; can be enhanced with phoneme analysis
    if spoken_text.strip().lower() == correct_sentence.strip().lower():
        return True, "Correct pronunciation!"
    else:
        return False, f"Incorrect pronunciation: Expected '{correct_sentence}', got '{spoken_text}'"
