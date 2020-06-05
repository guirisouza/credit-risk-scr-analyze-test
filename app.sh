#!/bin/sh
gunicorn -w 1 -b "127.0.0.1:8004" -t 300 app