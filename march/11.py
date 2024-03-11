from collections import defaultdict


def custom_sort_string(order: str, s: str):
    order_dict = defaultdict(int)
    for i, o in enumerate(order):
        order_dict[o] = i
    return ''.join(sorted(s, key=lambda x: order_dict[x]))

order = "cba"
s = "abcd"
print(custom_sort_string(order, s))