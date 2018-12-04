#!/bin/sh
echo "#################"
echo "Start of program"
echo "################"
mkdir mapreduce_results
python3 aprioriMapReduce.py data/5k.txt
echo "#################"
echo "Done 5"
echo "################################"
python3 aprioriMapReduce.py data/10k.txt
echo "#################"
echo "Done 10 "
echo "################################"
python3 aprioriMapReduce.py data/25k.txt
echo "#################"
echo "Done 25 "
echo "################################"
python3 aprioriMapReduce.py data/50k.txt
echo "#################"
echo "Done 50"
echo "################################"
python3 aprioriMapReduce.py data/100k.txt
echo "#################"
echo "Done 100"
echo "################################"
python3 aprioriMapReduce.py data/350k.txt
echo "################################"
echo "Rules can be found in rules.txt"
echo "################################"