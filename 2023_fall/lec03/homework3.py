

def cancellation(list, stop_word):
    '''
    Copy elements one by one from input_list into output_list. 
    If one of the elements is equal to the stop_word, then stop the function,
    and return what you have so far.
    '''

    output_list = []

    for x in input_list:
        output_list.append(x)
        if x == stop_word:
            break
        output_list.append(x)
    return output_list

def copy_all_but_skip_word(input_list, skip_word):
    '''
    This function should copy elements one by one from input_list into output_list.
    If one of the elements is equal to the skip_word, then you should skip that element,
    but keep checking all of the other elements.
    '''
    output_list = []

    for x in input_list:
        if x != skip_word:
            output_list.append(x)

    return output_list

def my_average(input_list):
    '''
    You may assume that `input_list` is a non-empty list, in which every element is a number.  
    Calculate the average value, and return it. 
    '''
    total = 0
    count = 0

    for number in input_list:
        if isinstance(number, (int, float)):
            total += number
            count += 1

    if count == 0:
        return 0  # Handle the case where there are no valid numbers in the list to avoid division by zero.
    
    average = total / count
    return average


