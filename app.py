from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from 

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
    return render_template('home.html')

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
        'created_at': datetime.now()
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

@app.route('/playlists/<playlist_id>')
def playlists_show(playlist_id):
    playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
    playlist_comments = comments.find({'playlist_id': ObjectId(playlist_id)})
    return render_template('playlists_index.html', playlist=playlist, comments=playlist_comments)

@app.route('/playlists/<playlist_id>', methods=['post'])
def playlists_update(playlist_id):
    videos_ids = request.form.get('videos_ids').split()
    videos = video_url_creator(videos_ids)

    update_playlist = {
        'title': request.form.get('title'),
        'descrption': request.form.get('description'),
        'videos': videos,
        'video_ids': video_ids
    }

    playlists.update_one(
        {'_id': ObjectId(playlist_id)},
        {'$set': updated_playlist})
    return redirect(url_for('playlists_show', playlist_id=playlist_id))

@app.route('/playlists/<playlist_id>/delete', methods=['post'])
def playlists_delete(playlist_id):
    playlists.delete_one({'_id': ObjectId(playlist_id)})
    return redirect(url_for('playlists_index'))

@app.route('/playlists/comments/comments', methods=['post'])
def comments_new():
    comment = {
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        'playlist_id': ObjectId(request.form.get('playlist_id')),
    }
    print(comment)
    comment_id = comments.insert_one(comment).inserted_id
    return redirect(url_for('playlists_show', playlist_id=request.form.get('playlist_id')))

@app.route('/playlists/comments/<comment_id>', methods=['post'])


if __name__ == '__main__':
    app.run(debug=True)