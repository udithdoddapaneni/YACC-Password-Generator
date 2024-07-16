from CustomRandom.RandomNumberGenerator import Randint

def RandomChoice(sequence):

    length = len(sequence)

    if(length==0):
        return "Sequence is Empty"

    random_index = Randint(0,length-1)

    return sequence[random_index]


# l = "fsdfdsfdwfeg"
# print(RandomChoice(l))

def RandomShuffle(list_to_shuffle):

    length = len(list_to_shuffle)

    for i in range(0,length-1,1):

        j = Randint(i,length-1)

        list_to_shuffle[i], list_to_shuffle[j] = list_to_shuffle[j], list_to_shuffle[i]



# x = [1,2,3,4]
# RandomShuffle(x)
# print(x)

def RandomChoices(sequence,k):

    length = len(sequence)

    if(k>length):
        return "Your Sequence size is less than required element"

    result_list = []
    index_list = []


    while(len(result_list)<k):

        random_index = Randint(0,length-1)
        if random_index in index_list:
            continue
        else:
            result_list.append(sequence[random_index])
            index_list.append(random_index)
    

    return result_list
    
# x = ['gdsgds','gds','vxzvx','tyityi']
# print(RandomChoices(x,4))
