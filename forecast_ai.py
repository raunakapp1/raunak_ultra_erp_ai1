import sqlite3
import numpy as np

DB_PATH = "database/erp.db"

def predict_tomorrow_revenue():
    """
    Simple AI logic:
    - Last 7 days ka average nikalega
    - Uspar trend factor lagake kal ka estimate dega
    """

    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        cur = conn.cursor()

        cur.execute("""
            SELECT total_amount FROM billing
            ORDER BY bill_date DESC
            LIMIT 7
        """)

        rows = cur.fetchall()
        conn.close()

        if not rows:
            return 0

        data = [r[0] for r in rows]

        avg = np.mean(data)
        growth_factor = 1.08   # 8% organic growth assumption

        prediction = int(avg * growth_factor)
        return prediction

    except Exception as e:
        return 0
