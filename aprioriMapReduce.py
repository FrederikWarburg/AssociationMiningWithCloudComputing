from mrjob.job import MRJob
from mrjob.step import MRStep
import itertools
import sys
import numpy as np
import time

# Global variables
SIZE_OF_FREQ_ITEM_SET = 2
#MINIMUM_CONFIDENCE = 0.5
#MINIMUM_SUPPORT = 2

class aprioriMapReduce(MRJob):
    
    def configure_args(self):
        super(aprioriMapReduce, self).configure_args()
        self.add_passthru_arg(
            '--min_supp', type=int, default=2, help='Minimum Support')
        self.add_passthru_arg(
            '--min_conf', type=int, default=0.5, help='Minimum Confidence')
        self.add_passthru_arg(
            '--freq_size', type=int, default=2, help='Size of Frequent itemsets')
                
    # First mapper that generates up to SIZE_OF_FREQ_ITEM_SET itemset.
    def freq_mapper(self, _, text_file):

        text_file = text_file.replace('"', '').replace(" ", "").split(",")
        items = text_file[1:]
        # generate the number of itemsets
        for item in items:
            yield [item], 1

        itemsets = itertools.combinations(items, self.options.freq_size)
        for p in itemsets:
            yield p, 1

    # Reduce all the incomming itemsets by counting their frequency.
    def freq_reducer(self, page, value):
        support = sum(value)
        yield page, support

    # Map all subpatterns of a given itemset, including the support of each subpattern
    # Yield the item and all itemsets it is in
    def subset_map(self, page, support):
        if len(page) > 1:    # Yield every subpattern in the page.
            for item in page:
                others = [i for i in page if i != item]
                #print(others, (page,support))
                yield others, (page, support)
        else:
            yield page, [support]

    # Combine the itemsets, so that each left value is described by the rest of the values.
    def subset_reducer(self, left, values):
        tempt = list(values)
        left_side = left[0]
        # calculate full support by going through the list of values
        full_support = 0
        for value in tempt:
            if isinstance(value[0], int):
                full_support = value[0]
                tempt.remove(value)

        # Go through each pattern and their corrosponding subpaterns.
        if full_support > self.options.min_supp:
            for i in range(len(tempt)):
                right_side = ""
                for item in tempt[i][0]:
                    if item != left_side:
                        right_side += item
                support = tempt[i][1]
                confidence = support / full_support
                # Print rules if they have high confidence and above minimum support.
                if confidence >= self.options.min_conf and support > self.options.min_supp:
                    rule = { 'left': left_side, 'right': right_side,
                        'sup': support, 'conf': np.round(confidence,2)}
                    print(rule)


    # Define the steps
    def steps(self):
        return [
            MRStep(mapper=self.freq_mapper,
                   reducer = self.freq_reducer),
            MRStep(mapper = self.subset_map,
                    reducer = self.subset_reducer)
        ]


if __name__ == '__main__':

    t1 = time.time()
    aprioriMapReduce.run()
    print(time.time() - t1)