# Complete the function below.

def get_rock_index(quantity):
    jamie = quantity
    ned = sorted(quantity)
    geoffrey = [x + y for x, y in zip(jamie, ned)]
    # print(jamie)
    # print(ned)
    # print(geoffrey)
    freq = dict()
    for i, x in enumerate(geoffrey):
        if x not in freq:
            freq[x] = {'count': 1, 'highest_index': i}
        freq[x]['count'] += 1
        freq[x]['highest_index'] = i
    max_num = -1
    max_count = -1
    # print(freq)
    for key, value in freq.items():
        if value['count'] == max_count:
            max_num = max(key, max_num)
        if value['count'] > max_count:
            max_num = key
            max_count = value['count']

    return freq[max_num]['highest_index']



