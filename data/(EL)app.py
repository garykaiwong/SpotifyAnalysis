from flask import Flask
from flask import render_template
import pandas as pd
import json

app = Flask(__name__)
@app.route('/')
def dance():
   url = 'topten.csv'
   dance= pd.read_csv(url)

   title = "TopTen Songs Danceability"
   Songs = dance[['name']]
   value = dance[['danceability']]


if __name__ == '__main__':
    app.run(debug=True)
   

