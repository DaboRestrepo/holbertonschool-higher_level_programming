#!/bin/bash
# Display the response body, only if status was 200.
curl -sX GET "$1" -L 200
