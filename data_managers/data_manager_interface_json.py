import json
import self as self
from .data_manager_interface import DataManagerInterface
import json
import os

# Define the path to the data.json file
data_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')


def file_data(filename):
    with open(filename, "r") as fileObject:
        json_data = fileObject.read()
        data = json.loads(json_data)
    return data

class JSONDataManager(DataManagerInterface):
    def __init__(self, filename):
        self.filename = filename

    def get_all_users(self):
        # Return all the users all users
        data = file_data(self.filename)
        users_list = [value['name'] for key, value in data.items()]
        return users_list

    def get_all_users_id(self):
        data = file_data(self.filename)
        users_id_list = [int(key) for key, value in data.items()]
        return users_id_list

    def get_all_movies_id(self, user_id):
        data = file_data(self.filename)
        user_movie_id_list = []
        for key, value in data.items():
            if int(key) == user_id:
                user_movie_id_list.append(value["movies"]["movie_id"])
                continue
        return user_movie_id_list


    def get_user_movies(self, user_id):
        # Return all the movies for a given user
        data = file_data(self.filename)
        user_movie_list= []
        for key, value in data.items():
            if int(key) == user_id:
                user_movie_list = value["movies"]
        return user_movie_list




obj = JSONDataManager(data_file_path)
x=obj.get_all_movies_id("")
print(x)