from collections import Counter

def find_most_common_word(file_path):
    # Read the file
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        # Split the text into words
        words = text.split()

        # Count the occurrences of each word
        word_counts = Counter(words)

        # Find the most common word
        most_common_word, count = word_counts.most_common(1)[0]

        return most_common_word, count
    except FileNotFoundError:
        return None, None

# Get filename from user input
file_path = input("Enter the filename: ")
most_common_word, count = find_most_common_word(file_path)

if most_common_word is not None:
    print(f"The most common word in '{file_path}' is '{most_common_word}' with {count} occurrences.")
else:
    print(f"File '{file_path}' not found.")
