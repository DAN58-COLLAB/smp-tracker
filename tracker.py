def predict_tomorrow_steps(steps):
    if len(steps) < 2:
        return "Not enough data"

    prediction = (steps[-1] + steps[-2]) / 2

    return round(prediction)