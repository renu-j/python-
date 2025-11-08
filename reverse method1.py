sentence = "I love Python"

# Step 1: Split the sentence into words
words = sentence.split()   # ['I', 'love', 'Python']

# Step 2: Reverse each word using slicing
reversed_words = [word[::-1] for word in words]   # ['I', 'evol', 'nohtyP']

# Step 3: Join them back into a single sentence
reversed_sentence = ' '.join(reversed_words)

print(reversed_sentence)
