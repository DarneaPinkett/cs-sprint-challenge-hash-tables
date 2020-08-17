#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

dict = {}        


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    arr = []

    for ticket in tickets:
        dict[ticket.source] = ticket.destination

    arr.append(dict['NONE'])

    for x in range(length):
        if arr[x] in dict:
            if dict[arr[x]] == arr[0]:
                continue
            arr.append(dict[arr[x]])
        

    return arr


# create emptry array.
# for each ticket in the ticket array, 
# add the ticket source as the key, 
# and the ticket destination as the value
