import numpy as np
from collections import Counter


def calculate_statistics(berry_data):
    return {
        "berries_names": berry_data['names'],
        "min_growth_time": min(berry_data['growth_times']),
        "median_growth_time": np.median(berry_data['growth_times']),
        "max_growth_time": max(berry_data['growth_times']),
        "variance_growth_time": np.var(berry_data['growth_times']),
        "mean_growth_time": np.mean(berry_data['growth_times']),
        "frequency_growth_time": dict(Counter(berry_data['growth_times'])),
    }
