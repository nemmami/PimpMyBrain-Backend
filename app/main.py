from flask import Flask, jsonify, request

from flask_cors import CORS

from routes import courses, users, ratings, favorites, authentications, notifications, chat_rooms, categories

app = Flask(__name__)
cors = CORS(app)

app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

# Routes
app.register_blueprint(courses.route, url_prefix="/courses")
app.register_blueprint(users.route, url_prefix="/users")
app.register_blueprint(ratings.route, url_prefix="/ratings")
app.register_blueprint(favorites.route, url_prefix="/favorites")
app.register_blueprint(notifications.route, url_prefix="/notifications")
app.register_blueprint(authentications.route, url_prefix="/authentications")
app.register_blueprint(chat_rooms.route, url_prefix="/chat_rooms")
app.register_blueprint(categories.route, url_prefix="/categories")

if __name__ == '__main__':
    app.run()
