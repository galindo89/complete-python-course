# library to read and write csv files
import csv

# Init Variables
movie_library = []
csv_file = "Movie_Library.csv"  # Define CSV file where to store library
csv_columns = ["name", "director", "year"]  # define the key values for the dictionary that will be store in a CSV file
search_menu = {
    "1": "name",
    "2": "director",
    "3": "year"
}  # Menu option when user wants to search in the movie library

# Load Movie_Library list of dictionaries with key name,director and year from a CSV
with open(csv_file) as file_object:
    reader = csv.DictReader(file_object, delimiter = ",")
    for row in reader:
        movie_library.append(dict(row))

# function to add new movies
def insert_new_movie():
    new_movie ={key: input(f"Insert please movie {key}:")
                for key in csv_columns}
    movie_library.append(new_movie)

        # store info in CSV
    try:
        with open(csv_file, 'w') as file_object:
            writer = csv.DictWriter(file_object, fieldnames = csv_columns)
            writer.writeheader()
            for data in movie_library:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    return movie_library

# function to print movie library
def print_movie_library(movie_library):
    for movie in movie_library:
        print("""-------------------------
        Movie Info
        """)
        for key, value in movie.items():
            print(f"{key}: {value}.")

# function to search for the movies based on search criteria selected by the user
def movie_searcher():
    search_by = input("Please search by: name [enter 1], director [enter 2], year [enter 3]: ")

    if search_by in search_menu:
        search_criteria = search_menu[search_by]
        movie_search = input(f"Enter {search_criteria}: ")
        filtered_movie = [movie for movie in movie_library if movie[search_criteria] == movie_search]
        print_movie_library(filtered_movie)
        # return filtered_movie
    else:
        print("Please enter a value between 1 and 3")
        movie_searcher()

# Program Starts

print("""Welcome to your movie library : 
			to add a movie press 1
			to search for your movies in the library press 2
			to print the list of all movies you have press 3
			to exit the program press 4	
			""")

while True:

    option = input("Please tell us what you want to do: ")

    if option == "1":
        insert_new_movie()

    elif option == "2":
        movie_searcher()
        # print_movie_library(movie_searcher())

    elif option == "3":
        print_movie_library(movie_library)

    elif option == "4":
        print("Thanks for using the library")
        break

    # in case user inputs something different to 1-4
    else:
        print("Please select an option between 1 and 4")
