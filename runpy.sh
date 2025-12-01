#!/bin/bash
day="$1"
shift || true

if [ -z "${day}" ]; then
    echo 'need day'
    exit 1
fi
day="$(echo ${day} | awk -F '/' '{print $1}')"

uv run python -m "${day}.py" "$@"