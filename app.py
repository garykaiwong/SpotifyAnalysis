from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
engine = create_engine("sqlite:///database.sqlite")


conn = engine.connect()

agg_year_data= pd.read_sql("SELECT * FROM data_by_year", conn)

tracks_data = pd.read_sql("SELECT * FROM tracks WHERE popularity>2",  conn)
tracks_data['year'] = tracks_data['release_date'].str[:4].astype(int)
tracks_data.head()

last_decade = tracks_data.loc[tracks_data['year'] >= 2010]
last_decade



@app.route("/")
def start():
    return render_template('page.html')

@app.route("/explicit_vs_popularity")
def explicit_popularity():

    explicit_df = pd.read_sql_query("""SELECT AVG(explicit) as 'avgExplicit', AVG(popularity) as 'avgPopularity', artists
                    FROM tracks
                    GROUP BY artists
                    HAVING AVG(popularity)>6;""", engine)


    print(explicit_df)               
    results = explicit_df.to_dict(orient="records")
    print(len(results))
    return jsonify(results)

@app.route("/most_explicit_tracks")
def explicit_tracks():

    explicit_df = pd.read_sql_query("""SELECT explicit, popularity, artists, name
                    FROM tracks
                    ORDER BY explicit DESC
                    LIMIT 20;""", engine)
    


if __name__ == '__main__':
    app.run(debug=True)
