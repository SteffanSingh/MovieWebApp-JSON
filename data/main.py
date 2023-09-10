
import csv
import json



with open("data.json", "r") as fileObject:
    data = json.loads(fileObject.read())


# Define the CSV file name
csv_file_name = "data.csv"

# Create and open the CSV file in write mode
with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["person_id", "person_name", "movie_id", "movie_name", "director", "year", "rating"])

    # Write data rows
    for person_id, person_data in data.items():
        person_name = person_data["name"]
        movies = person_data["movies"]

        for movie in movies:
            movie_id = movie["id"]
            movie_name = movie["name"]
            director = movie["director"]
            year = movie["year"]
            rating = movie["rating"]

            # Write movie data
            writer.writerow([person_id, person_name, movie_id, movie_name, director, year, rating])
