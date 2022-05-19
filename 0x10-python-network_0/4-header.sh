#!/bin/bash
# Send extra information to the request.
curl -s -H "X-School-User-Id:98" -X GET "$1"
