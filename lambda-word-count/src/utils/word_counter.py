def count_words(text):
    """Counts the number of words in a given text."""
    if not text:
        return 0
    words = text.split()
    return len(words)