# Program to store user's 3 favourite movies in a list

# Create an empty list
favourite_movies = []

# Ask user to enter their 3 favourite movies
for i in range(3):
    movie = input(f"Enter the name of your favourite movie {i+1}: ")
    favourite_movies.append(movie)

# Display the list of movies
print("\nYour favourite movies are:")
print(favourite_movies)
