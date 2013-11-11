#!/bin/sh

# upload CSV file to postgreSQL
#
#
# Make sure you have a table like this:
#  CREATE TABLE hourly
#  (
#    startdate timestamp without time zone NOT NULL,
#    enddate timestamp without time zone NOT NULL,
#    value double precision,
#    CONSTRAINT "startEndDate" PRIMARY KEY (startdate , enddate )
#  )

if [ $# -ne 3 ]; then
    echo "Usage: $0 dbname username csv_file"
    exit -1
fi

dbname="$1"
username="$2"
filename="$3"
psql $dbname $username << EOF
SET datestyle = "ISO, DMY";
COPY hourly FROM '$filename' DELIMITER ',' CSV HEADER;
EOF
