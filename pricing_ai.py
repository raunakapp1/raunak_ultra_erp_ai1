def dynamic_price(base, demand):
    multiplier = 1 + (demand * 0.05)
    return int(base * multiplier)