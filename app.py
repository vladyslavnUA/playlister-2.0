from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    #submit a new playlist
    print(request.form.to_dict())
    return redirect(url_for('playlists_index'))

@app.route('/playlists/new')
def playlists_new():
    #create a new playlist
    return render_template('playlists_new.html')

if __name__ == '__main__':
    app.run(debug=True)
