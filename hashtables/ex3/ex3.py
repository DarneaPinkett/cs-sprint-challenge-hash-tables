def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    new_lst = len(arrays)
    result = []

    for x in arrays:
        for i in x:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
                if dict[i] == new_lst:
                    result.append(i)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
