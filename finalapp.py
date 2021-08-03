from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
import pandas as pd
import pymongo
from tracks import results


app = Flask(__name__)
#engine = create_engine("sqlite:///database.sqlite")
#database_path = "database.sqlite"
#URI = f"sqlite:///{database_path}"

#engine = create_engine(URI)
#conn = engine.connect()
URI = f"sqlite:///database.sqlite"
engine = create_engine(URI)
conn = engine.connect()

#agg_year_data= pd.read_sql("SELECT * FROM data_by_year", conn)

@app.route("/")
def main():
    return render_template('main.html')


@app.route("/list")
def lister():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.songsDB

    songs_pull= db.songs.find()

    intel = songs_pull[0]['data']
    
    return render_template('harlanindex.html', intel = intel)

@app.route("/evp")
def explicit_popularity():

    #explicit_df = pd.read_sql_query("""SELECT explicit, popularity, artists, name, release_date, duration_ms, danceability
    #FROM tracks
    #WHERE popularity>2
    #ORDER BY popularity DESC
    #LIMIT 100""", engine)

    #explicit_df['year'] = explicit_df['release_date'].str[:4].astype(int)
    #last_decade = explicit_df.loc[explicit_df['year'] >= 2010]



    #print(last_decade)               
    #results = last_decade.to_dict(orient="records")
    #results=jsonify(results)

    f = {}
    for r in range(0, 99):
        f[f'{r}'] = results[r]


    return f

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
