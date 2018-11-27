#!/bin/sh
echo "#################"
echo "Start of program"
echo "################"

mkdir tmp
python3 WordFrequency.py Data/3mil.csv > tmp/userdata.txt

echo "###################"
echo "Finished 1'st step"
echo "###################"

python3 aprioriMapReduce.py tmp/userdata.txt > tmp/rules.txt

echo "################################"
echo "Rules can be found in rules.txt"
echo "################################"