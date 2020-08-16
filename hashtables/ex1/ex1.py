def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    
    for index in range(length):
        x = limit - weights[index]

        if x in dict:
            subtract = dict[x]

            new_lst = [index, subtract]
            new_lst.sort(reverse=True)
            return new_lst
        else:
            dict[weights[index]] = index

    return None



# empty dict
# go over the length of the of the weights
# calculate by substracting the value at the current index
# check the cache
#  if the value is in the cache extract it and assign to a new variable
