def count_letters(text):
    """Count the number of letters in the text."""
    return sum(c.isalpha() for c in text)

def count_words(text):
    """Count the number of words in the text."""
    return sum(c.isspace() for c in text) + 1  # Adding 1 for the last word

def count_sentences(text):
    """Count the number of sentences in the text."""
    return text.count('.') + text.count('!') + text.count('?')

def calculate_coleman_liau_index(letters, words, sentences):
    """Calculate the Coleman-Liau index based on letters, words, and sentences counts."""
    L = (letters / words) * 100
    S = (sentences / words) * 100
    return 0.0588 * L - 0.296 * S - 15.8

def determine_grade_level(index):
    """Determine the U.S. grade level based on the Coleman-Liau index."""
    grade = round(index)
    if grade < 1:
        return "Before Grade 1"
    elif grade >= 16:
        return "Grade 16+"
    else:
        return f"Grade {grade}"

def main():
    # Prompt the user to enter text
    text = input("Enter text: ")

    # Calculate counts needed for the index
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate the Coleman-Liau index
    index = calculate_coleman_liau_index(letters, words, sentences)

    # Determine and print the grade level
    grade_level = determine_grade_level(index)
    print(grade_level)

# Ensure the script is executed directly, not imported
if __name__ == "__main__":
    main()

# Example output for provided text: "Grade 3"
