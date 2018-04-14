#!/usr/bin/env sh

set -e

COUNTER=0
for D in $(cat classes)
do
    for F in $(find val/$D/ -type f)
    do
        echo "$(readlink -n -e $F) $COUNTER" >> val.txt
    done
    let COUNTER=COUNTER+1
done

COUNTER=0
for D in $(cat classes)
do
    for F in $(find train/$D/ -type f)
    do
        echo "$(readlink -n -e $F) $COUNTER" >> train.txt
    done
    let COUNTER=COUNTER+1
done

for F in $(find train/zzz_others/ -type f)
do
    echo "$(readlink -n -e $F) $COUNTER" >> train.txt
done
