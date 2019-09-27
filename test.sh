#!/bin/bash

echo "Local IP:    $(hostname -i)" && echo "External IP: $(wget -qO- http://ipecho.net/plain | xargs echo)"