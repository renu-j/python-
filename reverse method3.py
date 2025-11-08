#  Program: Reverse Words or Whole Sentence

def reverse_each_word(sentence):
    """Return a new sentence with each word reversed."""
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


def reverse_whole_sentence(sentence):
    """Return the entire sentence reversed (character by character)."""
    return sentence[::-1]


def main():
    print(" String Reversal Program ")
    print("-" * 45)

    # Ask for input
    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print(" Please enter a valid sentence.")
        return

    # Show menu options
    print("\nChoose an option:")
    print("1️.  Reverse each word")
    print("2️. Reverse the entire sentence")

    # Get user's choice
    choice = input("Enter your choice (1 or 2): ").strip()

    # Perform action based on choice
    if choice == "1":
        result = reverse_each_word(sentence)
        print("\n Each Word Reversed ")
        print(result)

    elif choice == "2":
        result = reverse_whole_sentence(sentence)
        print("\n Entire Sentence Reversed ")
        print(result)

    else:
        print(" Invalid choice! Please enter 1 or 2.")

    print("-" * 45)


#  Run the program
if __name__ == "__main__":
    main()
