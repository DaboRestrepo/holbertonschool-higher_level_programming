#!/bin/bash
# Display all the HTTP methods the server will accept.
curl -siX OPTIONS "$1" | awk '/Allow/{print substr($0, 8)}'
