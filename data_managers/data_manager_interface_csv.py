import csv
from .data_manager_interface import DataManagerInterface


def file_data(filename):
    with open(filename, "r") as fileObject:
        csv_data = fileObject.read()

    return csv_data
class CSVDataManager(DataManagerInterface):
    def __init__(self, filename):
        self.filename = filename

    def get_all_users(self):
        # Return all the users all users
        data = file_data(self.filename)
        users_list = [value["name"] for key, value in data.items()]
        return users_list

    def get_user_movies(self, user_id):
        # Return all the movies for a given user
        data = file_data(self.filename)
        user_movie_list = []
        for key, value in data.items():
            if int(key) == user_id:
                user_movie_list = value["movies"]
        return user_movie_list
