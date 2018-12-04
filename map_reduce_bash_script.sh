#!/bin/sh
echo "Start of program"
mkdir tempt
python3 WordFrequency.py data/"$@".csv > tempt/"$@".txt
echo "Finished first part"
mkdir mapreduce_results
python3 aprioriMapReduce.py tempt/"$@".txt > mapreduce_results/"$@".txt
echo "all done - rules can be found in mapreduce_results folder"
