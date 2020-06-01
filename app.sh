#!/bin/sh
gunicorn -w 1 -b "0.0.0.0:3000" -t 300 app

