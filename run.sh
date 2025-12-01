#!/bin/bash 
# usage: ./run.sh <impl> <day> [args...]
#
# eg.
#   ./run.sh py day01
#   ./run.sh go day01

impl="$1"
shift || true
day="$1"
shift || true

if [ -z "${impl}" ]; then
    echo 'need impl'
    exit 1
fi
if [ -z "${day}" ]; then
    echo 'need day'
    exit 1
fi

day="$(echo ${day} | awk -F '/' '{print $1}')"
if [ ! -d "${day}" ]; then
    echo "day ${day} not found"
    exit 1
fi
if [ ! -d "${day}/${impl}" ]; then
    echo "day ${day} implementation ${impl} not found"
    exit 1
fi

case "${impl}" in
    'py')
        uv run python -m "${day}.${impl}" "$@"
        ;;
    'go')
        go run "${day}/${impl}/main.go" "$@"
        ;;
    *)
        echo "don't know how to run impl ${impl}"
        exit 1
        ;;
esac
