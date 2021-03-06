# app.py
from flask import Flask, render_template, request
from pandas import read_csv
import plotly.express as px
from plotly.utils import PlotlyJSONEncoder
import json
import numpy as np

faithful = read_csv('./data/faithful.csv')
app = Flask(__name__)

@app.route('/graph', methods=['GET'])
def hist():
  # calculate the bins
  x = faithful['waiting']
  counts, bins = np.histogram(x, bins=np.linspace(np.min(x), np.max(x), int(request.args['bins'])+1))
  print("counts is ",counts)
  print("bins are ",bins)
  bins = 0.5* (bins[:-1] + bins[1:])
  print("bins are ",bins)
  p = px.bar(
    x=bins, y=counts,
    title='Histogram of waiting times',
    labels={
      'x': 'Waiting time to next eruption (in mins)',
      'y': 'Frequency'
    },
    template='simple_white'
  )
  print("p is ", p)
  return json.dumps(p, cls=PlotlyJSONEncoder)

@app.route('/')
def home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run()