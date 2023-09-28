#!/bin/bash
# make a request to 0:5000/catch_me to make server respond with message
curl -sLX PUT -d 'user_id=98' -H "origin:School" "0.0.0.0:5000/catch_me"
