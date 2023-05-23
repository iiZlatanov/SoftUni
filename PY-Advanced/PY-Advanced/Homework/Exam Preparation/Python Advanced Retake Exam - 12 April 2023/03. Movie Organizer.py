a = 5
b = 6
def movie_organizer(*args):
    collection_dict = {}
    for movie, genre in args:
        if genre not in collection_dict:
            collection_dict[genre] = []
        collection_dict[genre].append(movie)

    sorted_result = sorted(collection_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for genre, movie_name in sorted_result:
        sorted_movies = sorted(movie_name)
        result += f"{genre} - {len(movie_name)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"

    return result.strip()



# print(movie_organizer(
#     ("The Matrix", "Sci-fi")))

# print("")
#
# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))
#
# print("")

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))