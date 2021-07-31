from flask import Flask, render_template, url_for
import pymongo


app = Flask(__name__)

@app.route("/")
def start():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.songsDB

    songs_pull= db.songs.find()

    intel = songs_pull[0]['data']
    
    return render_template('harlanindex.html', intel = intel)

@app.route("/trts")
def new():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.traitsDB

    traits_pull= db.traits.find()

    intel = traits_pull[0]

    intel.pop('_id', None)
    
    return render_template('try.html', intel = intel)




if __name__ == '__main__':
    app.run(debug=True)
