#!/bin/bash

start_worker() {
    local queue=$1

    eval "rq worker -u redis://127.0.0.1:6379 $queue --path ./"
}
array=( comments comments comments comments )
for i in "${array[@]}"; do start_worker "$i" & done