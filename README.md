ea_scrape
=========

Scrape half-hourly smart meter data from Energy Australia's eWise website to a CSV as eWise does
not currently support the provision of data as CSV.

Instructions
============

Run ./download.sh to get html files downloaded and converted to (one) JSON file & (one) CSV file  
`Usage: download.sh username password from(yyyy/mm/dd)`  
  This will create a store directory and generate a bunch of files yyyy-mm-dd.html in there,
and also create all.json and all.csv files. Downloading approx a year's worth of data took 25-30 minutes last time I did it.

To create a graph of all electricity usage from start to end:  
`gnuplot plot_time.gnuplot > all.png`

To upload to a postgreSQL DB:  
`Usage: ./upload_pgsql.sh dbname username csv_file`  
  This will upload to your DB (see upload_pgsql.sh source for more details) and allow SQL queries to be executed against the data e.g.:

- to sum by date: `select startDate::DATE, sum(value) from hourly group by startDate::DATE`
- to get average, min, max by time of day: `select startDate::TIME, avg(value), min(value), max(value) from hourly group by startDate::TIME`

This has been tested on Mac OS X 10.7.5 with python 2.7.1. Your mileage may vary. 

TODO: 

- Known bug: if you provide incorrect login details the script will not warn you, it will just download garbage, and you will get nothing in your JSON and CSV files
