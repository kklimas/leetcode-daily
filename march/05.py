def solution(s):
    l, r = 0, len(s) - 1
    while s[l] == s[r] and l < r:
        print(f'BEFORE L: {l} R: {r}')
        ch = s[l]
        while s[l] == ch and l < r:
            if s[l + 1] == ch and l + 1 != r:
                l += 1
            else:
                break
        while s[r] == ch and l < r:
            if s[r - 1] == ch and l != r - 1:
                r -= 1
            else:
                break

        if l < r:
            l += 1
            r -= 1
        print(f'AFTER L: {l} R: {r}')
        print()
    return r - l + 1


print(solution('cabaabac'))
