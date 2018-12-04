# Association Mining With Cloud Computing

This GitHub repository is a implementation of the apriori algorithm for generating associtation rules used for the course 02807 "Computational tools for datascience"

----
In order to run the implenetation run the bashscript mapreduce_bash_script

The script can take arguments for the dataset. so specify which dataset that is going to be used and parse that as arguments.

The avaiable datasets can be seen in the data folder.

It's not recommend to run datasets greater than 350k rows, as MrJob writes tmp files to your machine that fills up your hardisk

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
In this repo a few files used for result analysation are left in, for the reader to go over


