e1 = '010'
e2 = '0101'


def solution(s):
    n = len(s)
    one_counter = 0
    for c in s:
        if c == '1':
            one_counter += 1
    return '1' * (one_counter - 1) + '0' * (n - one_counter) + '1'


print(solution(e1))