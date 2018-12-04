# Association Mining With Cloud Computing

This GitHub repository is an parallelize implementation of the Apriori algorithm with MapReduce for generating associtation rules used for the course 02807 "Computational tools for datascience"

----
In order to run the implenetation run the bash script mapreduce_bash_script

The script takes an dataset in csv format as arguments, so please specify which dataset that is going to be used and parse that as arguments.

The available datasets can be seen in the data folder.

It's not recommend to run datasets greater than 350k rows on a personal machine, as MrJob caches tmp files to your machine that fills up your hardisk. The large files should only be run in the cloud. To try a small example:

``
Sh mapreduce_bash_script.sh 5k
``

The rules can be found in a folder generated called mapreduce results 

----
The packages used are 

``
mrjob
``
``
numpy
``

---
In this repository a few files used for result analysation are left in, for the reader to go over. From these the results.ipynb it is seen that our parallelized Apriori implementation is faster than a baseline Apriori implementation for low support values.


