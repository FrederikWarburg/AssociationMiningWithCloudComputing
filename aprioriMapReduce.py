from mrjob.job import MRJob
from mrjob.step import MRStep
import numpy as np
import time

class aprioriMapReduce(MRJob):

    def configure_args(self):
        super(aprioriMapReduce, self).configure_args()
        self.add_passthru_arg(
            '--min_supp', type=int, default=2, help='Minimum Support')
        self.add_passthru_arg(
            '--min_conf', type=int, default=0.3, help='Minimum Confidence')
        self.add_passthru_arg(
            '--freq_size', type=int, default=2, help='Size of Frequent itemsets')

    def freq_mapper(self, _, text_file):
        text_file = text_file.replace('"', '').replace(" ", "").split(",")
        items = text_file[1:]
        # generate the number of itemsets
        items = list(items)
        for page1 in items:
            yield [page1], (1, items)

    def freq_reducer(self, page1, values):
        values = list(values)
        support1 = 0
        pages = []
        for value in values:
            support1 += value[0]
            pages.extend(value[1])
        if support1 > self.options.min_supp:
            yield page1, (support1, sorted(pages))

    def combination_mapper(self, page1, values):
        values = list(values)
        support1 = values[0]
        others = values[1]
        for page2 in others:
            if page2 != page1[0]:
                support2 = others.count(page2)
                if support2 > self.options.min_supp:
                    yield [page1[0], page2], (1, support1, support2, others)

    def combination_reducer(self, itemset, values):
        values = list(values)
        itemset_supp = 0
        for value in values:
            itemset_supp += value[0]
        if itemset_supp > self.options.min_supp:
            support1 = values[0][1]
            conf_a2b = itemset_supp / support1
            if conf_a2b > self.options.min_conf:
                left_side = itemset[0]
                right_side = itemset[1]
                rule = {'left': left_side, 'right': right_side,
                        'sup': itemset_supp, 'conf': np.round(conf_a2b, 2)}
                print(rule)

    # Define the steps
    def steps(self):
        return [
            MRStep(mapper=self.freq_mapper,
                   reducer=self.freq_reducer),
            MRStep(mapper=self.combination_mapper,
                   reducer=self.combination_reducer)
        ]


if __name__ == '__main__':
    # Time taking out commented
    # t1 = time.time()
    aprioriMapReduce.run()
    # Time taking out commented
    # print(time.time() - t1)