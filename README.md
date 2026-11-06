# Step Movement Predictor

A small Python learning project that estimates tomorrow's step count using the average of the two most recent daily step totals.

## What it does

The `predict_tomorrow_steps(steps)` function:
- Requires at least two recorded step counts.
- Calculates the mean of the latest two values.
- Rounds the estimate to the nearest whole step.
- Returns a helpful message when there is not enough data.

## Requirements

- Python 3.10 or newer
- No third-party packages required

## Usage

```python
from tracker import predict_tomorrow_steps

recent_steps = [6500, 8200, 7600]
prediction = predict_tomorrow_steps(recent_steps)

print(f"Predicted steps for tomorrow: {prediction}")
```

With fewer than two entries:

```python
print(predict_tomorrow_steps([6500]))
# Not enough data
```

## Current limitation

This is a beginner-friendly baseline, not a trained machine-learning model. It uses only the two latest values and does not account for trends, weekdays, activity patterns, or other factors.

## Possible improvements

- Validate that step counts are non-negative numbers.
- Add tests for normal and edge cases.
- Compare the two-day average with longer moving averages.
- Load step history from a CSV file or API.

## Project structure

```
smp-tracker/
├── tracker.py
├── README.md
└── .gitignore
```

## Learning goals

This project practices Python functions, lists, indexing, conditionals, arithmetic, rounding, and returning values.

## License

No license has been specified yet.
