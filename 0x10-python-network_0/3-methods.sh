#!/bin/bash
# Display all the HTTP methods the server will accept.
curl -siX OPTIONS "$1" | awk '/Allow/{print $2, $3, $4}'
