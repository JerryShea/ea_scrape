ea_scrape
=========

Scrape half-hourly smart meter data from Energy Australia's eWise website to a CSV as eWise does
not currently support the provision of data as CSV.

Instructions
============

Run ./download.sh to get html files downloaded and converted to (one) JSON file & (one) CSV file  
`Usage: download.sh username password from(yyyy/mm/dd)`  
  This will create a store directory and generate a bunch of files yyyy-mm-dd.html in there,
and also create all.json and all.csv files 

This has been tested on Mac OS X 10.7.5 with python 2.7.1. Your mileage may vary.

TODO: 

- Upload script to suck data into postgreSQL & misc SQL for data analysis
- Upload scripts to graph data using gnuplot
- Known bug: if you provide incorrect login details the script will not warn you, it will just download garbage, and you will get nothing in your JSON and CSV files
