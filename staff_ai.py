def staff_score(sales):
    return min(100, int(sales / 1000 * 10))