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
def precip():
    one_year = dt.date(2017, 8, 23)-dt.timedelta(days = 365)
    oy_precip = session.query(measurements.date, measurements.prcp).filter(measurements.date>=one_year).all()
    session.close()
    precip = []
    for date, prcp in oy_precip:
        pcp_dict = {}
        pcp_dict["Date"]=date
        pcp_dict["Precipitation (in)"]=prcp
        precip.append(pcp_dict)
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    results=session.query(station.station).all()
    session.close()
    stations=list(np.ravel(results))
    return jsonify(stations)

@app.route("/api/v1.0/tobs") 
def tobs():
    one_year = dt.date(2017, 8, 23)-dt.timedelta(days = 365)
    results = session.query(measurements.tobs).filter(measurements.station=="USC00519281").filter(measurements.date>=one_year).all()
    session.close()
    temp_obs=list(np.ravel(results))
    return jsonify(temp_obs)

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
