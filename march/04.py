def bag_of_tokens_score(tokens, power):
    n = len(tokens)
    l, r, score = 0, n - 1, 0

    # n*log(n)
    tokens.sort()

    while l < r and tokens[l] <= power:
        power -= tokens[l]
        l += 1
        score += 1

        # check if score > 0 and power is too small to gu further and power can be gained using right index
        tmp_score = score
        tmp_power = power
        while l < r and tmp_score > 0 and tokens[l] > tmp_power:
            tmp_power += tokens[r]
            r -= 1
            tmp_score -= 1

        if tokens[l] <= tmp_power:
            power = tmp_power
            score = tmp_score

    if l == r and tokens[l] <= power:
        score += 1

    return score


tokens = [100]
power = 50
print(bag_of_tokens_score(tokens, power))