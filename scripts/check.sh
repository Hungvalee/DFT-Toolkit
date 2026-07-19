#!/usr/bin/env bash

echo "======================================="
echo "DFT Toolkit Environment Check"
echo "======================================="

check_program () {

    if command -v "$1" >/dev/null 2>&1
    then
        printf "%-12s : OK\n" "$1"
    else
        printf "%-12s : NOT FOUND\n" "$1"
    fi
}

check_program python3
check_program mpirun
check_program phonopy
check_program vaspkit

echo
echo "Finished."
