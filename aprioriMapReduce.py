from mrjob.job import MRJob
from mrjob.step import MRStep
#import numpy as np
import itertools

SIZE_OF_FREQ_ITEM_SET = 3
class aprioriMapReduce(MRJob):
    #
    def freq_mapper(self, _, text_file):
        text_file = text_file.split(",")
        #user = text_file[0]
        items = text_file[1:]
        itemsets = itertools.combinations(items, SIZE_OF_FREQ_ITEM_SET )
        for p in itemsets:
            yield p, 1

    def fp_reducer(self, page, value):
        support = sum(value)
        yield page, support

    def fp_to_association_map(self, page, support):
        if support > 2:
            #yield page, support  # Yield the full pattern
            if len(page) > 1:    # Yield every subpattern
                for item in page:
                    others = [i for i in page if i != item]
                    yield others, (page, support)
            else:
                yield page, support


    def fp_to_association_reduce(self, left, values):
        tempt = list(values)
        for i in range(len(tempt)):
            support = tempt[i][1]
            right = ""
            for k in range(SIZE_OF_FREQ_ITEM_SET-1):
                right += tempt[i][0][k+1]
            left = tempt[i][0][0]
            full_support = 0
            for value in tempt:
                full_support += value[1]
            confidence = support / full_support
            rule = { 'right': right, 'left': left,
                    'sup': support, 'conf': confidence}
            print(rule)


    def steps(self):
        return [
            MRStep(mapper=self.freq_mapper,
                   reducer = self.fp_reducer),
            MRStep(mapper = self.fp_to_association_map,
                    reducer = self.fp_to_association_reduce)
        ]


if __name__ == '__main__':
    aprioriMapReduce.run()