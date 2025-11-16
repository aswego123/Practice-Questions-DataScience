import pandas as pd

df = pd.read_csv("q-python-cohort-retention.csv")

# Filter earliest cohort
cohort = df[df['signup_month'] == "2024-01"]

# Cohort size = customers active at month 0
cohort_size = cohort[cohort['month_offset'] == 0]['customer_id'].nunique()

# Active customers in month 3
active_m3 = cohort[
    (cohort['month_offset'] == 3) &
    (cohort['active_flag'] == 1)
]['customer_id'].nunique()

# Retention
retention_m3 = active_m3 / cohort_size
print(retention_m3)
