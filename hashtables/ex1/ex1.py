#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # go through list of weights
    for i in range(length):
        # check to see if there is a hash existing
        index_1 = hash_table_retrieve(ht, limit - weights[i])
        # if there is a hash, that means a pair exists
        if index_1 is not None:
            #return tuple of pair of indexes
            index_2 = (i, index_1)
            return index_2
        else:
            hash_table_insert(ht, weights[i], i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
