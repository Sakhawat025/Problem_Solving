def longestCommonPrefix(strs : list[str]) -> str:
    if not strs:
        return ""

    strs.sort()
    first = strs[0]
    last = strs[-1]
    result =[]

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            break
        result.append(first[i])

    return "".join(result)

s = input("enter Strings: ")
sTo_list = [String.strip() for String in s.split(",")]
res = longestCommonPrefix(sTo_list)
print(f'Longest comon prefix: "{res}"')