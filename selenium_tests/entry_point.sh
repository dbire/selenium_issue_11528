#!/bin/bash

echo "Welcome to the Python selenium test executor"

# shellcheck disable=SC2164

cd /app

testcase="$1"

# shellcheck disable=SC2236
if [ ! -z "$testcase" ]
then
    if [ ! -f "$testcase" ]
    then
        testcase_full_path=$(find /app -name "${testcase}".py)
    fi
    if [ -f "${testcase_full_path}" ]
    then
        echo "Running test script: ${testcase_full_path}"
        mkdir -p "./xml"
        # shellcheck disable=SC2086
        python -u ${testcase_full_path}
    else
        echo "ERROR: Cannot find a test script named ${testcase}.py in /app sub dirs"
    fi
fi