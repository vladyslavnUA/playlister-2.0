from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists


app = Flask(__name__)


@app.route('/')
def index():
    #homepage
    return render_template('home.html', msg='flask is cool')

# mock array of projects
# playlists = [
#     { 'title': 'cat videos', 'description': 'cats acting weird'},
#     { 'title': '80\'s music', 'description': 'don\'t stop believing!'}
# ]

@app.route('/playlists')
def playlists_index():
    #index playlists
    return render_template('playlists_index.html', playlists=playlists.find())

if __name__ == '__main__':
    app.run(debug=True)
