import numpy as np
import itertools as it

INDEX_FILE = "indexation/links_incidence_index.txt"
LINKS_FILE = "index.txt"
RESULT_RANK_FILE = "weighting/page_rank.txt"
ITERATIONS_NUM = 300
RESIDUAL_PROB = 0.85

with open(LINKS_FILE) as file:
    links = file.read().split()

with open(INDEX_FILE) as file:
    index = np.array([line.split() for line in file.readlines()]).astype(int)

# initial page ranks
page_ranks = [1 / len(links)] * len(links)

for _ in it.repeat(None, ITERATIONS_NUM):
    new_ranks = [0] * len(links)

    for i in range(len(links)):
        # indexes of docs that have link to current index doc
        linked_to_doc_indexes = np.where(index[:,i] != 0)[0]

        # sum of ratios:
        # ∀ doc ∈ linked_to_doc: doc page rank / num outbound links
        pr_ratios_sum = sum(page_ranks[x] / sum(index[x, :])
                           for x in linked_to_doc_indexes)

        # this iteration ranks count
        new_ranks[i] = (1 - RESIDUAL_PROB) / len(links) \
                        + RESIDUAL_PROB * pr_ratios_sum

    page_ranks = new_ranks

with open(RESULT_RANK_FILE, "w") as result_file:
    for doc_link, rank in zip(links, page_ranks):
        result_file.write("{link} {rank}\n".format(link=doc_link, rank=rank))