def merge_ranges(range_list):
    range_list = sorted(range_list, key=lambda x: x[0])
    final_list = list()
    start = range_list[0][0]
    end = range_list[0][1]
    for i, tup in enumerate(range_list):
        if end >= tup[0]:
            end = max(end, tup[1])
        else:
            final_list.append((start, end))
            start = tup[0]
            end = tup[1]
        # print('Start: ' + str(start) + ' End: ' + str(end))
        if i >= len(range_list) - 1:
            final_list.append((start, end))

    return final_list

if __name__ == '__main__':
    print(merge_ranges(  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
    print(merge_ranges(  [(1, 2), (2, 3)]))
    print(merge_ranges(  [(1, 5), (2, 3)]))
    print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))