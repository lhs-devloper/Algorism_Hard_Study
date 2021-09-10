def merge_split(data):
    if len(data) <= 1:
        return data

    medium = int(len(data) / 2)
    left = merge_split(data[:medium])
    right = merge_split(data[medium:])

    return merge(left, right)


def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged
