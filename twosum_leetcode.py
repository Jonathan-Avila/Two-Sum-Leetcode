#!/usr/bin/env python3

def twoSumList(nums, target):
    second_element = None
    for first_index, first_element in enumerate(nums):
        difference = target - first_element

        try:
            nums[first_index] = None
            second_index = nums.index(difference)
            second_element = nums[second_index]

        except ValueError:
            pass

        if second_element != None:
            return [first_index, second_index]

def twoSumDict(nums, target):
    a_dict = {}
    for index, element in enumerate(nums):
        complement = target - element
        if element in a_dict.keys():
            return [index, a_dict[element]]
        a_dict[complement] = index

def main():
    print(twoSumList([1,2,3,4], 4))
    print(twoSumList([1,6,10,8], 16))
    print(twoSumList([8,2,3,15], 23))
    print(twoSumList([40,2,60,55], 100))

    print(twoSumDict([1,2,3,4], 4))
    print(twoSumDict([1,6,10,8], 16))
    print(twoSumDict([8,2,3,15], 23))
    print(twoSumDict([40,2,60,55], 100))

main()
