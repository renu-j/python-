
# Ask the user to enter their own sentence
sentence = input("Enter any sentence: ")

# Step 1: Split the sentence into words
words = sentence.split()

# Step 2: Reverse each word using slicing
reversed_words = [word[::-1] for word in words]

# Step 3: Join them back into a single sentence
reversed_sentence = ' '.join(reversed_words)

# Step 4: Display the result
print("Reversed words sentence:", reversed_sentence)
