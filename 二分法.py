def binary_search(nums_list, num):
    low = 0
    height = len(nums_list) - 1
    while height >= low:
        # mid = low + (height - low) // 2
        mid = (low+height) // 2
        mid_num=nums_list[mid]
        if mid_num == num:
            return mid
        elif mid_num > num:
            height = mid-1
        else:
            low = mid+1
    return -1

if __name__ == '__main__':
    res = binary_search([1,2,3,5,10],12)
    print(res)
