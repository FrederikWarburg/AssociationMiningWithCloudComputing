# Association Mining With Cloud Computing

This GitHub repository is a Python3 implementation of the Apriori algorithm for generating associtation rules using MapReduce, developed for use in the DTU course 02807: "Computational tools for Data Science".

----
In order to run the implenetation, run the bashscript mapreduce_bash_script

The script can take arguments for the dataset. So remember to specify which dataset is going to be used and pass that as an argument.

The avaiable datasets can be found in the data folder.

It is not recommended to run this implementation for datasets greater than 350k rows, as MRJob writes a large amount of massive temporary files to your machine, which will quickly fill up your storage.

``
Sh mapreduce_bash_script.sh 5k
``

The generated association rules can be found in the automatically created folder "mapreduce results"

----
The required packages for running this implementation are

``
mrjob
``
``
numpy
``

---
Included in this repo are a few files used for data visualization and analysis, if the reader is interested.

