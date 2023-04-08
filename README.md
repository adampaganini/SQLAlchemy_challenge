# SQLAlchemy Module 10 Challenge

# Part 1: Analyzing and Explore the Climate Data

In this section, Python and SQLAlchemy was used to do a basic climate analysis and data exploration of a climate database. Specifically, SQLAlchemy ORM queries, Pandas, and Matplotlib were used to complete the analysis in the [climate_starter.ipynb](https://github.com/adampaganini/SQLAlchemy_challenge/blob/main/climate_starter.ipynb) file. SQLAlchemy was used to create an engine function to connect to the SQLite database called [hawaii.sqlite](https://github.com/adampaganini/SQLAlchemy_challenge/blob/main/Resources/hawaii.sqlite). The two following analyses were conducted:

a) A **precipitation analysis** was conducted by finding the most recent date in the dataset, getting the previous 12 months of precipitation data, and plotting the precipitation results for that 12 month period as shown below.

![alt text](https://raw.githubusercontent.com/adampaganini/SQLAlchemy_challenge/main/images/precipitation.png)

b) Also, a **station analysis** was conducted by querying the data set to calculate the total number of stations, finding the most-active stations. Station 'USC00519281' has the greatest number of observations at 2,772. Next, a query was designed to calculate the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query. Those temperatures were 54.0 ºF, 71.7 ºF, and 85 ºF, respectively. A query was designed to get the temperature observation data, or "TOBS", by filtering by the station that has the greatest number of observations, and querying the previous 12 months of TOBS data for that station. A histogram of this data with bins=12 was generated as show below.

![alt text](https://raw.githubusercontent.com/adampaganini/SQLAlchemy_challenge/main/images/hist.png)

## Part 2: Designing a 'Climate App'

