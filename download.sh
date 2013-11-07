#!/bin/sh

# Download data from energy australia website, convert it to JSON & CSV
# This can take a few minutes

mkdir store 2> /dev/null

python download.py "$@"
#echo $?

# grep JSON from html and make it well-formed
cat store/*.html | grep -E '\"startDate\"|\"endDate\"|\"value\"' | ./eahtml_to_json.sh > store/all.json

# json->csv and grep out any null values
python json_to_csv.py store/all.json | grep -v ',[^0-9]$' > store/all.csv
