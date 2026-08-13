def  roman_to_integer(s: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total = 0
    s = s.strip().upper()
    length = len(s)

    for i in range(length):
        current_val = values[s[i]]

        if i + 1 < length  and current_val < values[s[i + 1]]:
            total -=current_val
        else:
            total += current_val
    return total

s = input("Enter String: ")
result = roman_to_integer(s)
print(result)