#!/bin/sh
echo "#################"
echo "Start of program"
echo "################"
python3 WordFrequency.py Data/3mil.csv > userdata.txt
echo "###################"
echo "Finished 1'st step"
echo "###################"
python3 aprioriMapReduce.py userdata.txt > rules.txt
echo "################################"
echo "Rules can be found in rules.txt"
echo "################################"