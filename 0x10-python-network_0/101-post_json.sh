#!/bin/bash
# send a JSON POST request to a url from a file and display body of the response
curl -sLX POST -d @"$2" -H 'Content-Type: application/json' "$1"
