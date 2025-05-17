from imdb import IMDb

def get_movie_rating():
    movie_name=input("Enter the name of the movie:")
    ia=IMDb()
    movie=ia.search_movie(movie_name)
    if movie:
                # Print the first result
        movie = movie[0]
        print(f"Title: {movie['title']}")
        ia.update(movie)
        print(f"Genres: {movie.get('genres')}")
        print(f"IMDB Rating: {movie.get('rating')}")
        print(f"Director(s): {[d['name'] for d in movie.get('director', [])]}")
    else:
        print("no movie found with this name")
get_movie_rating()       



