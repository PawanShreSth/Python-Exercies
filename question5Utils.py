# Method to print all movies rated above 9.0
def print_all_movies_above_9(list_of_movies):
    for i in range(len(list_of_movies)):
        if (list_of_movies[i][1] > 9.0):
            print(f"Movie whose rating is above 9.0: {list_of_movies[i][0]} \nRating: {list_of_movies[i][1]}")



# Method to get average ratings of all movies in a list
def get_avg_rating(list_of_movies):
    total_rating = 0

    for i in range(len(list_of_movies)):
        total_rating += list_of_movies[i][1]

    return total_rating / len(list_of_movies)



# Method to check if the movie is present in the dataset and obtains its rating if exists (Helper Method)
def check_moviecount_and_get_rating(str, movies):
    count_with_rating = [0, 0]

    for i in range(len(movies)):
        if (str.lower() == movies[i][0].lower()):
            count_with_rating[0] += 1
            count_with_rating[1] = movies[i][1]
    
    return count_with_rating



# Method to displaye the rating of the movie
def display_rating_of_entered_movie(movie_name, movie_ratings):
    movie_occurrence_count, movie_rating = check_moviecount_and_get_rating(movie_name, movie_ratings)

    if (movie_occurrence_count == 0):
        print("Entered movie's detail does not exist in the database. Please try again later.")
        return
    else:
        print(f"Rating of entered movie: {movie_rating}")