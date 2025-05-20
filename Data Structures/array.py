# Initialize array
arr: list[int] = [0] * 5
nums: list[int] = [1, 2, 3, 4, 5]


# Accessing elements -> O(1)
def access(nums: list[int], index: int) -> int:
    return nums[index]


# Inserting elements -> O(n)
def insert(nums: list[int], num: int, index: int) -> int:
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num
    return nums


# Deleting elements -> O(n)
def remove(nums: list[int], index: int) -> int:
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]
    return nums


# Traversing arrays -> O(n)
def traverse(nums: list[int]):
    # By index
    for i in range(0, len(nums)):
        print(nums[i])
    # By elements
    for num in nums:
        print(num)
    # By both index and elements
    for i, num in enumerate(nums):
        print(i, num)


# Finding elements -> O(n)
def find(nums: list[int], num: int):
    for i in range(len(nums)):
        if nums[i] == num:
            return i
    return -1

# Expanding arrays -> O(n)
def extend(nums: list[int], enlarge: int) -> list[int]:
    res = [0] * (len(nums) + enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res
