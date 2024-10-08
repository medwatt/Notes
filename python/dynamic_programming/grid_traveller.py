####################
## Grid Traveller ##
####################

### Brute-Force
def grid_traveller(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


### Memoized
def grid_traveller(m, n):
    memo = {"1,1": 1}

    def helper(m, n):
        if m == 0 or n == 0:
            return 0
        key = f"{m},{n}"
        if key in memo:
            return memo[key]
        key = f"{n},{m}"
        if key in memo:
            return memo[key]
        memo[key] = helper(m - 1, n) + helper(m, n - 1)
        return memo[key]

    return helper(m, n)


### Tabulation
def grid_traveller(m, n):
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[1][1] = 1
    for i in range(1, m):
        for j in range(1, n):
            table[i][j + 1] += table[i][j]
            table[i + 1][j] += table[i][j]
    # right-most column
    for i in range(1, m):
        table[i + 1][-1] += table[i][-1]
    # bottom row
    for j in range(1, n):
        table[-1][j + 1] += table[-1][j]
    return table[m][n]
