#!/bin/bash

start_worker() {
    local queue=$1

    eval "venv/bin/rq worker -u redis://127.0.0.1:6379 $queue --path ./"
}
array=( redditors subreddits submissions comments )
for i in "${array[@]}"; do start_worker "$i" & done