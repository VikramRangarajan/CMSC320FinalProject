import pandas as pd

"""
This script converts the csvs into parquets for smaller size
and faster loading times.

You need to install fastparquet (run "pip install fastparquet").
"""

for fn in ["job_skills", "job_summary", "linkedin_job_postings"]:
    pd.read_csv(f"{fn}.csv").to_parquet(f"{fn}.parquet")