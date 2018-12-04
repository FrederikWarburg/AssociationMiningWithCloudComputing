# Association Mining With Cloud Computing

This GitHub repository is a parallelized implementation of the Apriori algorithm with MapReduce in Python3 for generating associtation rules, used for the DTU course 02807: "Computational tools for Data Science"

----
In order to run the implenetation, run the bash script mapreduce_bash_script

The script takes a dataset in a .txt file in CSV format as argument, so please specify which dataset you would like to pass it as an argument

The available datasets can be found in the data folder.

It is not recommended to run this implementation for datasets greater than 350k rows on a personal machine, as MRJob caches temporary files to your machine, which will quickly fill up your storage. The large dataset files should only be run in the cloud. To try a small example:

``
Sh mapreduce_bash_script.sh 5k.txt
``

The generated association rules can be found in the automatically created folder called: mapreduce results 

----
The packages required to run this implementation are:

``
mrjob
``
``
numpy
``

---
In this repository a few files used for result visualization and analysis are left in, if the reader wishes to go over them. From the notebook results.ipynb it can seen that our parallelized Apriori implementation is faster than a baseline Apriori implementation for low support values.


