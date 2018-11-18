#!/bin/bash
for f in *.csv
do
    awk '{ print $5, $4 / $3 }'  > presentation/$f
done
