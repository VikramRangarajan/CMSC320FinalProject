import pandas as pd
import os

"""
This script converts the csvs into parquets for smaller size
and faster loading times.

You need to install fastparquet (run "pip install fastparquet").
"""

for fn in ["job_skills", "job_summary", "linkedin_job_postings"]:
    if not os.path.isfile(f"{fn}.parquet"):
        print(f"Reading {fn}.csv to {fn}.parquet...")
        pd.read_csv(f"{fn}.csv").to_parquet(f"{fn}.parquet")
        print(f"{fn}.parquet created!")
    else:
        print(f"{fn}.parquet already exists.")