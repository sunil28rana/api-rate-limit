#!/bin/bash
if [ ! -d redis-6.0.5/src ]; then
    curl -O http://download.redis.io/releases/redis-6.0.5.tar.gz
    tar xvzf redis-6.0.5.tar.gz
    rm redis-6.0.5.tar.gz
fi
cd redis-6.0.5
make
src/redis-server