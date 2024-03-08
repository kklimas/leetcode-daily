def char_map_sorted_props(word):
    res = dict()
    for c in word:
        if c in res:
            res[c] = res[c] + 1
        else:
            res[c] = 1

    return sorted(list(res.keys())), sorted(list(res.values()))


def close_strings(word1: str, word2: str) -> bool:
    k1, v1 = char_map_sorted_props(word1)
    k2, v2 = char_map_sorted_props(word2)
    return k1 == k2 and v1 == v2
