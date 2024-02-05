import timeit

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(value):
    count_coins = {}
    for coin in coins:
        count = value // coin
        if count > 0:
            count_coins[coin] = count
        value = value - coin * count    
    return count_coins


def find_min_coins(value):    
    min_coins_required = [0] + [float("inf")] * value  
    last_coin_used = [0] * (value + 1)
    for s in range(1, value + 1):
        for coin in coins:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin
    count_coins = {}
    current_sum = value
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum = current_sum - coin
    return count_coins


def benchmark(amounts):
    greedy_times = []
    dynamic_times = [] 
    for amount in amounts:
        greedy_times.append(timeit.timeit(lambda: find_coins_greedy(amount), number=1000))
        dynamic_times.append(timeit.timeit(lambda: find_min_coins(amount), number=1000))
    return [['Greedly', greedy_times], ['Dynamic', dynamic_times]]

 
def draw_table(results):    
    print(f"| {'Алгоритм':<16} | {'Час виконання'}")    
    print(f"| {'-'*16} | {'-'*13}")
    for result in results:
        mean = sum(result[1])/len(result[1])
        print(f"| {result[0]:<16} | {mean:<13.6f}")
  



if __name__ == "__main__":
    val = 113
    print(f'Cума: {val}')

    result_dynamic = find_min_coins(val)
    print(f'Монети [Greedle Algorithm]: {result_dynamic}')

    result_greedy = find_coins_greedy(val)
    print(f'Coins [Dynamic Algorithm]: {result_greedy}')

    print('\n\nМалі суми:\n' + '-'*40 )
    small_amounts = list(range(90, 99, 1))
    #draw_table(benchmark(small_amounts))
   
    print('\nСередні суми:\n' + '-'*40 )
    medium_amounts = list(range(990, 999, 1))
    #draw_table(benchmark(medium_amounts))

    print('\nВеликі суми:\n' + '-'*40 )
    big_amounts = list(range(9990, 9999, 1))
    #draw_table(benchmark(big_amounts))
   