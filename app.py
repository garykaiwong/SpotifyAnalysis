from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
engine = create_engine("sqlite:///data_by_year_.sqlite")



@app.route("/")
def start():
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
