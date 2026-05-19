def word_count(text):
    words = text.split()
    word_frequency = {}
    for word in words:
        word = word.lower()
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    return word_frequency

def main():
    text = """Python is a high-level, interpreted, general-purpose programming language.
              Its design philosophy emphasizes code readability with the use of significant indentation."""
    print("Given text:\n", text)
    counts = word_count(text)
    print("Word frequencies in the given text:")
    for word, count in counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
