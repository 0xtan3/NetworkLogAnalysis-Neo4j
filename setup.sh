#!/bin/bash

echo "Installing falkordb in docker..."
sudo docker run -p 6379:6379 -p 3000:3000 falkordb/falkordb