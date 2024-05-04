import itertools
import nltk
import json

# Download NLTK resources (word corpus)
nltk.download('words')

# Load English words set
english_words = set(nltk.corpus.words.words())

# Generate all two-letter combinations of the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
two_letter_combinations = [''.join(comb) for comb in itertools.combinations(alphabet, 2)]

# Find words formed by these combinations
word_combinations = {}
for comb in two_letter_combinations:
    words_for_comb = [word for word in english_words if comb in word]
    unique_words_for_comb = list(set(words_for_comb))  # Remove duplicates
    word_combinations[comb] = unique_words_for_comb

# Convert to JSON format
data = {'word_combinations': word_combinations}

# Save to JSON file
with open('word_combinations.json', 'w') as f:
    json.dump(data, f, indent=4)

print("JSON file created successfully.")
