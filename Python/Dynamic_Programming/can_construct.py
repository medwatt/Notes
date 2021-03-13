###################
## Can Construct ##
###################

### Brute-Force
def can_construct(target, word_bank):
    if target == "":
        return True
    for word in word_bank:
        if len(target) >= len(word) and target[: len(word)] == word:
            remainder = target[len(word) :]
            if can_construct(remainder, word_bank):
                return True
    return False


### Memoized
def can_construct(target, word_bank):
    memo = {}

    def helper(target, word_bank):
        if target == "":
            return True
        if target in memo:
            return memo[target]
        for word in word_bank:
            if len(target) >= len(word) and target[: len(word)] == word:
                remainder = target[len(word) :]
                if helper(remainder, word_bank):
                    memo[target] = True
                    return memo[target]
        memo[target] = False
        return False

    return helper(target, word_bank)


### Tabulation
def can_construct(target, word_bank):
    table = [False] * (len(target) + 1)
    table[0] = True
    for i in range(len(target)):
        if table[i]:
            for word in word_bank:
                if target[i : i + len(word)] == word:
                    table[i + len(word)] = True
    return table[-1]
