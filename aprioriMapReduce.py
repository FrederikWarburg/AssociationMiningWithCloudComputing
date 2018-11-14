from mrjob.job import MRJob
from mrjob.step import MRStep
import numpy as np
import itertools


class aprioriMapReduce(MRJob):
    #
    def freq_mapper(self, _, text_file):
        text_file = text_file.split(",")
        user = text_file[0]
        items = text_file[1:]
        itemsets = itertools.combinations(items, 2)
        for p in itemsets:
            yield p, 1

    def fp_reducer(self, page, value):
        support = sum(value)
        yield page, support

    def fp_to_association_map(self, page, support):
        yield page, support  # Yield the full pattern
        if len(page) > 1:    # Yield every subpattern
            for item in page:
                others = [i for i in page if i != item]
                yield others, list((page,support))

    def fp_to_association_reduce(self, left, values):
        rule = {}
        tempt = list(values)
        fullpattern_support = []
        for sets in tempt:
            if isinstance(sets, int):
                tempt.remove(sets)
                continue
            fullpattern_support = 5

        for value in tempt:
            pattern = value[0]
            support = value[1]
            confidence = float(support)/float(fullpattern_support)
            rule = { 'left': left, 'right': pattern, 
                    'sup': support, 'conf': confidence }
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