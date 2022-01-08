#!/bin/bash
# Displays HTTP methods the server will accept   
OPT=$(curl -sIX OPTIONS "$1" | grep "(Allow)") && echo "${OPT##*: }"
