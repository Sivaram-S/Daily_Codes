def find(list_input):
    for i in list_input:
        if i < 0:
            list_input[list_input.index(i)] = 0

    start_value = min(list_input)
    end_value = max(list_input)

    x = [i for i in range(start_value+1, end_value)]

    not_in = []

    is_in_list = lambda k: True if k in list_input else False

    for i in x:
        if not is_in_list(i):
            not_in.append(i)

    if not_in:
        return min(not_in)
    else:
        return max(list_input) + 1        
    
    
if __name__ == "__main__":
    l = find([3,4,2,1,-1,10])
    print(l)


