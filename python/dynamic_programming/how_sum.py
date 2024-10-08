#############
## How Sum ##
#############

### Brute-Force
def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    for num in numbers:
        remainder = target_sum - num
        if remainder >= 0:
            combination = how_sum(remainder, numbers)
            if combination is not None:
                combination = combination + [num]
                return combination
    return None


### Memoized
def how_sum(target_sum, numbers):
    memo = {}

    def helper(target_sum, numbers):
        if target_sum == 0:
            return []
        if target_sum in memo:
            return memo[target_sum]
        for num in numbers:
            remainder = target_sum - num
            if remainder >= 0:
                combination = helper(remainder, numbers)
                if combination is not None:
                    memo[target_sum] = combination + [num]
                    return memo[target_sum]
        memo[target_sum] = None
        return memo[target_sum]

    return helper(target_sum, numbers)


### Tabulation
def how_sum(targert_sum, numbers):
    table = [None] * (targert_sum + 1)
    table[0] = []
    for i in range(targert_sum):
        if table[i] is not None:
            numbers = [num for num in numbers if i + num <= targert_sum]
            for num in numbers:
                table[i + num] = table[i] + [num]
    return table[-1]
