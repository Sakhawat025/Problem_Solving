n = int(input())
coins = list(map(int, input().split()))

t_sum= sum(coins)
coins.sort(reverse = True)

my_sum = 0
coin_count = 0

for coin in coins:
    my_sum += coin
    coin_count += 1

    if my_sum > (t_sum - my_sum):
        break

print(coin_count)