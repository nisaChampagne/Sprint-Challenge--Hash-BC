#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    # route will be like capacity
    
    #loop through each ticket and insert them in the hashtable
    for ticket in tickets:
       hash_table_insert(hashtable, ticket.source, ticket.destination)

    location = hash_table_retrieve(hashtable, "NONE")

    for index in range(length):
        route[index] = location
        location = hash_table_retrieve(hashtable, location)

    return route
