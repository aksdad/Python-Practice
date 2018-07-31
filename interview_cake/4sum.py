def fourSum(nums, target):
    solution2 = []
    solution3 = []
    solution = []
    nums.sort()
    for ai, a in enumerate(nums):
        if ai > 0 and a == nums[ai - 1]:
            solution2 = two_sum(nums[ai + 1:], target - 2 * a, [a, a])
            if solution2: solution += solution2
        else:
            solution3 = three_sum(nums[ai + 1:], target - a, [a])
            if solution3: solution += solution3
    return solution


def three_sum(nums, target, a):
    solution = []
    for idx, tgt in enumerate(nums):
        if idx > 0 and nums[idx] == nums[idx - 1]: continue
        path = {}
        vist = set()
        for i in range(idx + 1, len(nums)):
            if nums[i] not in path:
                path[target - tgt - nums[i]] = nums[i]
            elif nums[i] in path and nums[i] not in vist:
                solution.append(a + [tgt, path[nums[i]], nums[i]])
                vist.add(nums[i])
    return solution


def two_sum(nums, target, b):
    path = {}
    solution = []
    for i in nums:
        if i in path:
            return solution.append(b + [path[i], i])
        else:
            path[target - i] = i
    return solution


def sum_4 (a, x):
    map = dict()
    return_result = []
    for i in range(len(a)):
        complement = x - a[i]
        a_2 = list(a)
        a_2.remove(a[i])
        print(str(a[i]) + " " + str(a_2) + " " + str(complement))
        indices = sum_3(a_2, -complement)
        if len(indices) != 0:
            for i in range(len(indices)):
                result = [indices[i][0], indices[i][1], indices[i][2], a[i]]
                result.sort()
                print(result)
                if result not in return_result:
                    return_result.append(result)

    return return_result

def sum_3 (a, x):
    map = dict()
    return_result = []
    for i in range(len(a)):
        complement = x - a[i]
        a_2 = list(a)
        a_2.remove(a[i])
        print(str(a[i]) + " " + str(a_2) + " " + str(complement))
        indices = sum_2(a_2, complement)
        if len(indices) != 0:
            result = [indices[0], indices[1], a[i]]
            result.sort()
            print(result)
            if result not in return_result:
                return_result.append(result)
    return return_result

def sum_2 (a, x):
    map = dict()
    result = list()
    for i in range(len(a)):
        if a[i] in map.keys():
            map[a[i]] += 1
        else:
            map[a[i]] = 1

    for i in range(len(a)):
        complement = x - a[i]
        if complement == a[i]:
            if complement in map.keys():
                map[a[i]] -= 1
        if complement in map.keys():
            if map[complement] > 0:
                return [a[i], complement]

    return []


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    print(sum_4(nums, target))