def remaining_intervals(collected_intervals, desired_interval):
    #Sort our array to make it easier to iterate through
    collected_intervals = sorted(collected_intervals, key = lambda x: x[0])

    #Final list to be returned
    ret = []

    #initialize variables
    last_start = desired_interval[0]
    last_end = None

    #Loop through the sorted list of intervals
    for interval in collected_intervals:
        cur_start = interval[0]
        cur_end = interval[1]

        #range check for the start of an interval
        if(cur_start < desired_interval[1]):

            #Check if the current interval is the first one we have looked at so far
            if(cur_start > last_start and last_end is None):
                ret.append((last_start, cur_start))
            elif (last_end is not None):
                    ret.append((last_end, cur_start))

            #prepare for next iteration
            last_start = cur_start
            last_end = cur_end

    #incase the last interval has an ending time less than the start time of the desired interval
    if last_end < desired_interval[1]:
        ret.append((last_end, desired_interval[1]))

    #finally, return the result!
    return ret

if __name__ == '__main__':
    print(remaining_intervals([(3, 4), (4,7), (7,9)], (1,12)))