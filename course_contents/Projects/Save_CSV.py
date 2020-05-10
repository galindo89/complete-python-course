import csv
csv_columns = ["name","director","year"]
movie_library = [

    {"name": "The Matrix", "director": "Wachowskis", "year": "1994"},
    {"name": "Kill Bill", "director": "Tarantino", "year": "1998"},
    {"name": "Indiana Jones", "director": "Steven Spielberg", "year": "1994"}

]
csv_file = "Testeo.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in movie_library:
            writer.writerow(data)
except IOError:
    print("I/O error")