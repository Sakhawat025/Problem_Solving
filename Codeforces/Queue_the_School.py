def transform_queue(s_list, n):
    i = 0
    while i < n - 1:
        if s_list[i] == "B" and s_list[i + 1] == "G":
            s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
            i += 2
        else:
            i += 1
    return s_list


if __name__ == "__main__":
    n, t = map(int, input().split())
    s = input()

    s_list = list(s)

    for _ in range(t):
        s_list = transform_queue(s_list, n)

    ans = "".join(s_list)
    print(ans)
