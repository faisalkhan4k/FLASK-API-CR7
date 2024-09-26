from flask import Flask
from data_ingest import df
app=Flask(__name__)


name='Mohammed fasial khan'

@app.route('/')
def hello():
    return 'Faisal'


app.run(debug=True)