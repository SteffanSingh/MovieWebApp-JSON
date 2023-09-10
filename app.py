from flask import Flask, jsonify,render_template,request,redirect, url_for
from data_managers.data_manager_interface_json import JSONDataManager
import  json
import  requests


movie_data = "data/data.json"
 

app = Flask(__name__)

data_manager = JSONDataManager(movie_data)



@app.route('/')
def home():
    return "Welcome to MovieWeb App!"

@app.route("/users")
def list_users():
    users_list = data_manager.get_all_users()
    return render_template("users.html", users=users_list)


@app.route("/users/<int:user_id>")
def user_movie_list(user_id):
    user_movies = data_manager.get_user_movies(user_id)
    return jsonify(user_movies)

@app.route("/add_user", methods = ["GET","POST"])
def add_user():
    if request.method == "POST":
        name = request.form['name']
        if name == None:
            return render_template("users.html")
        else:
            users_id_list = data_manager.get_all_users_id()
            user = {}
            id = max(users_id_list) + 1
            user[id]["name"] = name
            user_list = data_manager.get_all_users()
            user_list.append(name)
            return redirect(url_for("index"))

    return render_template("index.html")



@app.route("/users/<user_id>/add_movie", methods = ["POST"])
def add_user_movie(user_id):
    users_id_list = data_manager.get_all_users_id()
    user_list = data_manager.get_all_users()
    user = {}
    movie = {}
    name = request.form["name"]

    Key = "2837c90f"
    Url = f"http://www.omdbapi.com/?apikey={Key}&t={name}"
    res = requests.get(Url)
    data = res.json()
    movie["name"] = data["Title"]
    movie["rating"] = data["imdbRating"]
    movie["year"] = data["Year"]
    movie["director"] = data["Director"]

    for user in user_list:
        if user_id not in users_id_list:
            return render_template("users.html")
        elif user_id in users_id_list:
            index = users_id_list.index(user_id)
            user[user_id]["movies"].append(movie)
            render_template("add_movie.html")

@app.route("/users/<user_id>/update_movie/<movie_id>", methods = ["PUT"])
def update_movie(user_id, movie_id):
    pass

@app.route("/users/<user_id>/delete_movie/<movie_id>", methods = ["DELETE"])
def delete_movie(user_id, movie_id):
    pass



if __name__ == '__main__':
    app.run(debug=True)

