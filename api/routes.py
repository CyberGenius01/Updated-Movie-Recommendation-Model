from flask import render_template, redirect, request, url_for, flash, jsonify
from . import app
from recommender.algorithm import MovieRecommendation
from api.forms import UserInput
import threading
import requests
import json

task_status = {"completed": False}

with open('default-movies.json', 'r') as f:
    default_movies =  json.load(f)
movies = default_movies

headers = {
    'content-type': "application/json",
    'authorization': "YOUR KEY"
}

movies_lock = threading.Lock()

def fetchImages():
    global movies
    try:
        with movies_lock:
            for movie in movies:
                try:
                    req = requests.get(
                        f"https://api.collectapi.com/imdb/imdbSearchById?movieId={movie['imdb_id']}",
                        headers=headers
                    )
                    data = json.loads(req.text)
                    movie['image'] = data["result"].get("Poster", 'https://demofree.sirv.com/nope-not-here.jpg')
                except KeyError:
                    movie['image'] = 'https://demofree.sirv.com/nope-not-here.jpg'
                except Exception as e:
                    print(f"Error fetching image for {movie['imdb_id']}: {e}")
        task_status["completed"] = True
    except Exception as e:
        print(f"Unexpected error in fetchImages: {e}")
    

@app.route('/', methods=['GET', 'POST'])
def home_page():
    global task_status
    form = UserInput()
    if request.method == 'POST' and form.validate_on_submit():
        task_status["completed"] = False
        category = form.category.data
        value = form.value.data
        count = form.count.data
        return redirect(url_for('result_page', value=value, category=category, count=count))
    return render_template('base.html', form=form, movies=default_movies)



@app.route('/recommendations', methods=['GET', 'POST'])
def result_page():
    category = request.args.get('category')
    value = request.args.get('value')
    count = int(request.args.get('count'))

    global task_status
    form = UserInput()
    if request.method == 'POST' and form.validate_on_submit():
        task_status["completed"] = False
        category = form.category.data
        value = form.value.data
        return redirect(url_for('result_page', value=value, category=category))

    recommender = MovieRecommendation(category, value)
    global movies

    if not task_status['completed']: movies = recommender.recommend(count)
    
    if movies is not None:
        threading.Thread(target=fetchImages).start()
    else:
        flash('Data for the filter is unavailable in the database')
        movies = default_movies
    return render_template('recommended.html', movies=movies, form=form)

@app.route('/task-status', methods=['GET'])
def task_status_check():
    return jsonify(task_status)
