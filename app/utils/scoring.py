def aggregate_score(scores):
    numeric = [v for v in scores.values() if isinstance(v, (int, float))]
    return round(sum(numeric) / len(numeric), 2)
