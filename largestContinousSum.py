def largestContinousSum(arr):

    if(len(arr) == 0):
        return 0

    max_sum = current_sum = arr[0]
    start_index = end_index = 0

    for i, num in enumerate(arr[1:]):
        total_sum = current_sum+num
        if(total_sum > num):
            current_sum = total_sum

        else:
            current_sum = num
        #current_sum = max(current_sum+num, num)

        if(current_sum > max_sum):
            max_sum = current_sum
            end_index = i+1
        else:
            max_sum = max_sum
        #max_sum = max(current_sum, max_sum)

    print(max_sum)
    #print(start_index, end_index)
    return max_sum
largestContinousSum([-3, -6, -1, 4, -4, 2, -6, 3, -7, 2, 4, -7, 5])