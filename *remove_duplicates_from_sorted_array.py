def removeDuplicates(nums):
    unique = 1

    for index, element in enumerate(nums):
        if index < len(nums)-2 and nums[index] != nums[index + 1]:
            unique += 1
    return unique


def main():
    print(removeDuplicates([1,1,2,2]))

main()
