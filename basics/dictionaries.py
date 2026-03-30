def word_frequency(text: str) -> dict[str, int]:
    words = text.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


if __name__ == "__main__":
    sentence = "The cat ate the rat wearing a hat."
    print(word_frequency(sentence))