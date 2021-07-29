from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
import pandas as pd
import pymongo

app = Flask(__name__)
engine = create_engine("sqlite:///data_by_year_.sqlite")
database_path = "../data_by_year_o.sqlite"
URI = f"sqlite:///{database_path}

engine = create_engine(URI)
conn = engine.connect()

agg_year_data= pd.read_sql("SELECT * FROM data_by_year", conn)


@app.route("/")
def start():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.songsDB
    songs_pull= db.songs.find()
    important = songs_pull[0]['data']
    return render_template('page.html')

@app.route("/explicit_vs_popularity")
def explicit_popularity():

    explicit_df = pd.read_sql_query("""SELECT explicit, popularity 
                    FROM data_o
                    GROUP BY year;""", engine)
    results = explicit_df.to_json(orient="records")
    
    return results




if __name__ == '__main__':
    app.run(debug=True)
