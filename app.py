import os
import requests
from flask import Flask, render_template, request
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

movies = [{
'id': 1,
'title': 'Fuckyou',
'genre': 'blah'
}]

from models import Movies

@app.route('/movies', methods=['GET'])
def getMovie():
    return jsonify({'movies': movies})

# @app.route('/movies', methods=['POST'])
# def createMovie():
#     mov = Movies(request.json.get('title', ''), request.json.get('genre', ''))
#     db.session.add(mov)
#     db.session.commit()
#     return jsonify( {'movies': mov} ), 201


# @app.route('/movies', methods=['POST'])
# def createMOVE():
#     title = request.form['title']
#     genre = request.form['genre']
#
#     note = Note(title=title, genre=genre)
#
#     db.session.add(note)
#     db.session.commit()
#
#     return jsonify({note})

@app.route('/movies', methods=['POST'])
def createMovie():
    movie = {
        'id': movies[-1]['id'] +1,
        'title': request.json['title'],
        'genre': request.json['genre']
    }
    movies.append(movie)
    return jsonify({'movie':movie})

# @app.route('/movies/<int:id>')
# def get_dev(id):
#     return jsonify({'movies': movies.query.get(id)})


@app.route('/movies/<int:id>', methods=['PUT'])
def editMovie(id):
    movie = {
        'title': request.json['title'],
        'genre': request.json['genre']
    }
    db.session.commit()
    return jsonify( {'movies': movie})

@app.route('/movies/<int:id>', methods=['DELETE'])
def deleteMovie(id):
    db.session.delete(Movies.query.get(id))
    db.session.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run()
