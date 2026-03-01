def predict_tomorrow_revenue(today_revenue):
    try:
        return float(today_revenue) * 1.12
    except:
        return 0
