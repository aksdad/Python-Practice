def rectangle_intersection(r1, r2):
    x1 = r1['left_x']
    x2 = r2['left_x']
    w1 = r1['width']
    w2 = r2['width']

    y1 = r1['bottom_y']
    y2 = r2['bottom_y']
    h1 = r1['height']
    h2 = r2['height']

    left = max(x1, x2)
    right = min(x1 + w1, x2 + w2)

    if right <= left:
        return None

    bottom = max(y1, y2)
    top = min(y1 + h1, y2 + h2)

    if top <= bottom:
        return None

    new_rect = {
        # coordinates of bottom-left corner
        'left_x': left,
        'bottom_y': bottom,

        # width and height
        'width': right - left,
        'height': top - bottom,
    }

    return new_rect

if __name__ == '__main__':
    rect1 = {
        'left_x': 5,
        'bottom_y': 5,

        # width and height
        'width': 30,
        'height': 20,
    }

    rect2 = {
        'left_x': 10,
        'bottom_y': 10,

        # width and height
        'width': 30,
        'height': 20,
    }

    rect3 = {
        'left_x': 50,
        'bottom_y': 50,

        # width and height
        'width': 30,
        'height': 20,
    }

    print(rectangle_intersection(rect1, rect2))
    print(rectangle_intersection(rect1, rect3))
