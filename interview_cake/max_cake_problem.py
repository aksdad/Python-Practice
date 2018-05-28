def max_duffel_bag_value(cake_tuples, weight_capacity):

    max_value_at_capacity = [0] * (weight_capacity + 1)

    for capacity in range(weight_capacity + 1):
        max_value_at_current = 0

        for cake_weight, cake_value in cake_tuples:
            if cake_weight <= capacity:
                max_with_current_cake = (cake_value + max_value_at_capacity[capacity - cake_weight])
                max_value_at_current = max(max_value_at_current, max_with_current_cake)

        max_value_at_capacity[capacity] = max_value_at_current

    return max_value_at_capacity[weight_capacity]

if __name__ == '__main__':
    print(max_duffel_bag_value([(7, 160), (3, 90), (2, 15)], 20))
