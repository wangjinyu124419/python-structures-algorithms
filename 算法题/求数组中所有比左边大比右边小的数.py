"""
以时间复杂度O(n)从长度为n的数组中找出同时满足下面两个条件的所有元素：
（1）该元素比放在它左边的所有元素都大；
（2）该元素比放在它右边的所有元素都小。
"""

def find_nums(num_list):
    left_max = num_list[0]
    right_min = num_list[-1]
    left_set = set()
    right_set = set()
    for i in num_list:
        if i >=left_max:
            left_set.add(i)
            left_max = i
    for i in reversed(num_list):
        if i <=right_min:
            right_set.add(i)
            right_min = i
    target_set = left_set & right_set
    return target_set


if __name__ == '__main__':
    res=find_nums([1,2,5,3,6,10,20,40,30])
    print(res)



