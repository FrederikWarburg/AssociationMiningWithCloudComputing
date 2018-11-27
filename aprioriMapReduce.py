from mrjob.job import MRJob
from mrjob.step import MRStep
import itertools

# Global variables
SIZE_OF_FREQ_ITEM_SET = 2
MINIMUM_CONFIDENCE = 0.05
MINIMUM_SUPPORT = 1

class aprioriMapReduce(MRJob):

    # First mapper that generates up to SIZE_OF_FREQ_ITEM_SET itemset.
    def freq_mapper(self, _, text_file):
        text_file = text_file.split(",")
        items = text_file[1:]
        # generate the number of itemsets
        itemsets = itertools.combinations(items, SIZE_OF_FREQ_ITEM_SET)
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
                yield others, (page, support)
        else:
            yield page, support

    # Combine the itemsets, so that each left value is described by the rest of the values.
    def subset_reducer(self, left, values):
        tempt = list(values)
        left_side = left[0]
        # calculate full support by going through the list of values
        full_support = 0
        for value in tempt:
            full_support += value[1]

        if full_support < MINIMUM_SUPPORT:
            # Go through each pattern and their corrosponding subpaterns.
            for i in range(len(tempt)):
                right_side = ""
                for item in tempt[i][0]:
                    if item != left_side:
                        right_side += item
                support = tempt[i][1]
                confidence = support / full_support
                # Print rules if they have high confidence and above minimum support.
                if confidence > MINIMUM_CONFIDENCE and support > MINIMUM_SUPPORT:
                    rule = { 'left': left_side, 'right': right_side,
                            'sup': support, 'conf': confidence}
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
    aprioriMapReduce.run()