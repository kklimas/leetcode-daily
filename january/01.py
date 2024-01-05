"""
Assume you are an awesome parent and want to give your children some cookies.
 But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
 and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will
  be content. Your goal is to maximize the number of your content children and output the maximum number.
"""

children = [2, 1, 3]
sizes = [1, 1]


def find_content_children(children_cost, cookies_sizes):
    children_cost.sort()
    cookies_sizes.sort()

    child_i, cookie_i, content_children = 0, 0, 0
    while child_i < len(children_cost) and cookie_i < len(cookies_sizes):
        # cookie can be given to child
        if cookies_sizes[cookie_i] >= children_cost[child_i]:
            content_children += 1
            child_i += 1
            cookie_i += 1
            continue
        cookie_i += 1

    return content_children


print(find_content_children(children, sizes))
