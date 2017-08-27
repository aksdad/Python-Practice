def binary_search(target, nums):
    max_r = len(nums) - 1
    min_r = 0
    while min_r <= max_r:
        mid_r = min_r + (max_r - min_r) // 2
        if nums[mid_r] == target:
            return True
        if nums[mid_r] < target:
            min_r = mid_r + 1
        else:
            max_r = mid_r - 1
    return False

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    print(binary_search(0, nums))
