"""
You are given a dataset containing movie names and their corresponding ratings. 
Each entry in the dataset is represented by a tuple with the movie name as the first element and the rating as the second element.

movie_ratings = [ 	("Inception", 8.7),
("The Shawshank Redemption", 9.3),
("The Dark Knight", 9.0),
("Forrest Gump", 8.8),
("Pulp Fiction", 8.9),
      ]
Write a Python program that prints the names of movies with ratings above 9.0.
Calculate and print the average rating of all the movies.
Ask the user to enter the name of a movie and display its rating. Handle the case where the entered movie name is not in the dataset.

"""
import dataset
from question5Utils import print_all_movies_above_9, get_avg_rating, display_rating_of_entered_movie


def question_5(data_of_movie):
    print_all_movies_above_9(data_of_movie)
    print(f"Average ratings of movies in the database: {get_avg_rating(data_of_movie)}")

    movie_name_by_user = input("Enter the name of the movie to know its rating: ")
    display_rating_of_entered_movie(movie_name_by_user, data_of_movie)


question_5(dataset.movie_dataset)