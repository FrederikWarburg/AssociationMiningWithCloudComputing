from mrjob.job import MRJob
import numpy as np
class wordFrequency(MRJob):
    #
    def mapper(self, _, csv_file):

        csv_file = csv_file.split(",")
        user = csv_file[1]
        page = csv_file[3]

        yield user, page

    def reducer(self, user, pages):
        pagestring = ""
        for page in np.unique(list(pages)):
            pagestring += ", " + page
        yield user, pagestring

if __name__ == '__main__':
    wordFrequency.run()