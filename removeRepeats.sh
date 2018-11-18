#!/bin/bash
for f in *.csv
do
    sort -t, -u -k2,2 $f > NR_$f
done
