#!/bin/bash
# Display the Content-size.
curl -sI "$1" | awk '/Content-Length/{print $2}'
