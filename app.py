from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)

def video_url_creator(id_lst):
    videos = []
    for vid_id in id_lst:
        #embedded youtube videos
        video = 'https://youtube.com/embed/' + vid_id
        videos.append(video)
    return videos

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
    #grab video IDs and make a list out of them
    video_ids = request.form.get('video_ids').split()
    #call helper function
    videos = video_url_creator(video_ids)
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': videos,
        'video_ids': video_ids
    }
    playlists.insert_one(playlist)
    return redirect(url_for('playlists_index'))
    
    #submit a new playlist
    print(request.form.to_dict())
    return redirect(url_for('playlists_index'))

@app.route('/playlists/new')
def playlists_new():
    #create a new playlist
    return render_template('playlists_new.html')
 
if __name__ == '__main__':
    app.run(debug=True)