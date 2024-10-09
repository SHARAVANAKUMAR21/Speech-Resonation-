import pronouncing# Make sure to install this library

def phoneme_compare(spoken_text, correct_sentence):
    spoken_phonemes = get_phonemes(spoken_text)
    correct_phonemes = get_phonemes(correct_sentence)

    # Compare phonemes
    if spoken_phonemes == correct_phonemes:
        return True, "Correct pronunciation!"
    else:
        return False, f"Incorrect pronunciation: Expected '{correct_sentence}', got '{spoken_text}'"

def get_phonemes(text):
    words = text.split()
    phonemes = []
    for word in words:
        phoneme_list = pronouncing.phones_for_word(word)
        if phoneme_list:
            phonemes.append(phoneme_list[0])  # Get the first pronunciation
        else:
            phonemes.append("")  # No phonetic representation found
    return " ".join(phonemes)
