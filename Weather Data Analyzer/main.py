import numpy as np
from data import months, month_names
avg_months = np.array([np.mean(m) for m in months])

def mean_temp_month():
    for i in range (12):
        print(f"{month_names[i]}: {np.mean(months[i]):.2f}")

def min_temp_month():
    for i in range (12):
        print(f"{month_names[i]}: {np.min(months[i])}")
def max_temp_month():
    for i in range(12):
        print(np.max(months[i]))

def warmest_temp_month():
    idx = np.argmax(avg_months)
    return f"{month_names[idx]}: {avg_months[idx]:.2f}"

def coldest_temp_month():
    idx = np.argmin(avg_months)
    return f"{month_names[idx]}: {avg_months[idx]:.2f}"

print(warmest_temp_month())
print(coldest_temp_month())