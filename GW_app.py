from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
engine = create_engine("sqlite:///database.sqlite")


conn = engine.connect()

agg_year_data= pd.read_sql("SELECT * FROM data_by_year", conn)


@app.route("/")
def start():
    return render_template('page.html')

@app.route("/explicit_vs_popularity")
def explicit_popularity():

    explicit_df = pd.read_sql_query("""SELECT AVG(explicit) as 'avg explicit', AVG(popularity) as 'avg popularity', artists
                    FROM tracks
                    GROUP BY artists
                    HAVING AVG(popularity)>3;""", engine)
                    
    results = explicit_df.to_dict(orient="records")
    
    return jsonify(results)




if __name__ == '__main__':
    app.run(debug=True)
