n = int(input())

# The first element on each line is p (or q), followed by the levels
x_levels = list(map(int, input().split()))[1:]
y_levels = list(map(int, input().split()))[1:]

# Combine both sets of levels passed
passed_levels = set(x_levels) | set(y_levels)

if len(passed_levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")