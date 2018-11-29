#!/bin/sh
echo "#################"
echo "Start of program"
echo "################"
mkdir mapreduce_results
for i in 400 300 200 100 90 80 70 60 50 40 30 25 20 15 10
do
echo $i
python3 aprioriMapReduce.py --min_supp $i data/itemsets3mil.txt > mapreduce_results/$i.txt
done
echo "################################"
echo "Rules can be found in rules.txt"