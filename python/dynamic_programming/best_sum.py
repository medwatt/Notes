##############
## Best Sum ##
##############

## Brute-Force
def best_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        if remainder >= 0:
            combination = best_sum(remainder, numbers)
            if combination is not None:
                combination = combination + [num]
                if shortest_combination is None or len(combination) < len(
                    shortest_combination
                ):
                    shortest_combination = combination
    return shortest_combination


### Memoized
def best_sum(target_sum, numbers):
    memo = {}

    def helper(target_sum, numbers):
        if target_sum == 0:
            return []
        if target_sum in memo:
            return memo[target_sum]
        shortest_combination = None
        for num in numbers:
            remainder = target_sum - num
            if remainder >= 0:
                combination = helper(remainder, numbers)
                if combination is not None:
                    combination = combination + [num]
                    if shortest_combination is None or len(combination) < len(
                        shortest_combination
                    ):
                        shortest_combination = combination
        memo[target_sum] = shortest_combination
        return memo[target_sum]

    return helper(target_sum, numbers)


## Tabulation
def best_sum(targert_sum, numbers):
    table = [None] * (targert_sum + 1)
    table[0] = []
    for i in range(targert_sum):
        if table[i] is not None:
            numbers = [num for num in numbers if i + num <= targert_sum]
            for num in numbers:
                if table[i + num] is None or len(table[i]) < len(table[i + num]):
                    table[i + num] = table[i] + [num]
    return table[-1]
