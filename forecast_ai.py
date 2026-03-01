def predict_tomorrow_revenue(today_revenue):
    try:
        today_revenue = float(today_revenue)
        return today_revenue * 1.12
    except:
        return 0
