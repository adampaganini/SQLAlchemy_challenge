import numpy as np
import pandas as pd
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
measurements = Base.classes.measurement
station = Base.classes.station

session = Session(engine)

#setting up Flask app

app = Flask(__name__)

@app.route("/")
def welcome():
    return(f'''
    <h1>Welcome to the Hawaii Climate Analysis API!</h1><br/>
        Available Routes:<br/>
        /api/v1.0/precipitation<br/>
        /api/v1.0/stations<br/>
        /api/v1.0/tobs<br/>
        /api/v1.0/temp/start<br/>
        /api/v1.0/temp/start/end<br/>
        'start' and 'end' date should be in the format MMDDYYYY.<br/>
    ''')

@app.route("/api/v1.0/precipitation")


@app.route("/api/v1.0/stations")
def stations():
    results=session.query(station.station).all()
    session.close()
    stations=list(np.ravel(results))
    return jsonify(stations)

#@app.route("/api/v1.0/tobs") 


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def statistics(start=None, end=None):
    sel=[func.min(measurements.tobs), func.avg(measurements.tobs), func.max(measurements.tobs)]

    if not end:
        results=session.query(*sel).filter(measurements.date>=start).all()
        session.close()
        temps=list(np.ravel(results))
        return jsonify(temps)
    
    results=session.query(*sel).filter(measurements.date>=start).filter(measurements.date<=end).all()
    session.close()
    temps=list(np.ravel(results))
    return jsonify(temps)


if __name__ == '__main__':
    app.run()
