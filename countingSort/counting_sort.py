def counting_sort(nums):
    max_value = max(nums)
    num_counts = [0] * (max_value + 1)
    sorted_nums = []

    for num in nums:
        num_counts[num] += 1

    for num, counts in enumerate(num_counts):
        for _ in range(counts):
            sorted_nums.append(num)

    return sorted_nums

if __name__ == '__main__':
    nums = [8, 12, 4 , 4, 4, 6, 7, 8, 9, 4, 12,3, 5, 6,5, 64,5, 7, 86, 8,3 ,45, 9]
    print(counting_sort(nums))