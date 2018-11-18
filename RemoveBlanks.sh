#!/bin/bash
for f in *.csv
do
    awk -F, '{if ($1!="") print}' $f > NB_$f
done
