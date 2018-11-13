from mrjob.job import MRJob
import numpy as np
class aprioriMapReduce(MRJob):
    #
    def mapper(self, _, text_file):
        text_file = text_file.split(",")
        user = text_file[0]

        for i in range(1,len(text_file)):
            yield text_file[i], 1

    def reducer(self, page, value):

        yield page, sum(value)

if __name__ == '__main__':
    aprioriMapReduce.run()