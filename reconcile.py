def all_combinations(terms):
    sub_sets = [[]]
    for term in terms:
        without = []
        for sub_set in sub_sets:
            without.append(list(sub_set))
        for sub_set in sub_sets:
            sub_set.append(term)
        sub_sets.extend(without)
    return sub_sets

def reconcile(terms, total):
    for combination in all_combinations(terms):
        if sum(combination) == total:
            return combination
    return None

combinations = all_combinations([100])
assert combinations == [[100], []], "got {}".format(combinations)

combinations = all_combinations([100, 50])
assert combinations == [[100, 50], [50], [100], []], "got {}".format(combinations)

reconciled = reconcile([100, 50, 20, 5], 125)
assert reconciled == [100, 20, 5], "got {}".format(reconciled)

terms = [
    100,
    50,
    20,
    5,
]
total = 125
result = reconcile(terms, total)
if result:
    print "One valid combination is {}".format(result)
else:
    print "No valid combination."
