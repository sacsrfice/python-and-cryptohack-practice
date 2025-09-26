def galeShapley(men_prefs, women_prefs):
    counter = len(men_prefs)
    free_men = list(range(counter))
    engaged = [None] * counter  # Index: woman, Value: man
    men_next_proposal = [0] * counter  # Next woman to propose to for each man

    # Build inverse preference list for women for quick comparison
    women_rank = [
        {man: rank for rank, man in enumerate(women_prefs[w])}
        for w in range(counter)
    ]

    while free_men:
        m = free_men.pop(0)
        w = men_prefs[m][men_next_proposal[m]]
        men_next_proposal[m] += 1

        if engaged[w] is None:
            engaged[w] = m
        else:
            current = engaged[w]
            if women_rank[w][m] < women_rank[w][current]:
                engaged[w] = m
                free_men.append(current)
            else:
                free_men.append(m)

    # Build result as list of (man, woman) pairs
    result = [(engaged[w], w) for w in range(counter)]
    return result

# Example usage:
men_prefs = [[0,1,2], [2,1,0], [1,2,0]]
women_prefs = [[2,1,0], [0,1,2], [2,0,1]]
print(galeShapley(men_prefs, women_prefs))
