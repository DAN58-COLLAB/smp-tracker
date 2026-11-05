def calculate_daily_trend(steps):
    if len(steps) < 2:
        return "Not enough data"

    difference = steps[-1] - steps[-2]

    if difference > 0:
        return "Increasing"
    elif difference < 0:
        return "Decreasing"
    else:
        return "Unchanged"