Jobs in Demand 2025–26 — LinkedIn Job Market Analysis

This project analyzes a large sample of LinkedIn job postings (~100k rows) to understand which job roles, skills, technologies, and cloud platforms are most in demand in 2025–26.
The analysis includes title normalization, role/seniority classification, skill extraction, a role × skill matrix, and a skill-demand time series.


PROJECT GOALS

Identify which job titles appear most frequently

Normalize titles into broader roles (Engineer, Analyst, Assistant, Sales…)

Detect seniority levels (Junior, Senior, Lead, Unspecified)

Count mentions of key data & cloud skills across roles

Build a Role × Skill heatmap

Analyze monthly skill demand trends for technologies like Spark, GCP, and Snowflake

Export clean datasets for further analysis or visualization


REPOSITORY STRUCTURE

Folders:

notebooks

data

results

Files inside folders:

notebooks/

jobs_in_demand_analysis.ipynb

data/

sample_postings.csv

results/

titles_with_role_level.csv

skills_counts.csv

role_skill_counts.csv

top3_skills_by_role.csv

skill_trends_monthly.csv

root folder contains:

README.md

The full LinkedIn CSV is not included due to size limits.
A small sample dataset (sample_postings.csv) is provided for reproducibility.

METHODS AND PIPELINE

1. Data loading with encoding fallback

Automatic detection of encoding (utf-8 → fallback to latin1)

sep=None with engine="python" for flexible CSV parsing

Chunked loading (chunksize=50,000) for efficiency

2. Exploring and grouping job titles

Frequency count of top 15 job titles

Title normalization to lowercase and whitespace cleanup

3. Title → Role → Seniority classification

Each title is mapped to:

Role: Engineer, Analyst, Manager, Assistant, Accountant, Sales, Support/CS, Healthcare, or Other

Level: Senior, Junior, Lead/Principal, Unspecified

Classification uses:

A dictionary of hard-coded overrides

Keyword-based ROLE_KEYWORDS rules

4. Skill extraction from job descriptions

Tracked skills include:

["kafka","bigquery","spark","dbt","airflow","snowflake","mlops",
 "kubernetes","gcp","azure data factory","databricks"]

Counts are aggregated across:

All postings (skills_df)

Each role (role_skill_counts)

Top 3 per role (top3_by_role)

5. Role × Skill heatmap

Visualizing which roles are connected to which tools:

Engineers → Spark, Kubernetes, GCP, Databricks

Analysts → BigQuery, dbt, Snowflake

Sales/Managers → mostly cloud-platform mentions

Assistants & Support roles → minimal technical skill mentions

6. Skill demand over time

A time series of monthly mentions for:

Spark

GCP

Snowflake

This shows how cloud and data engineering technologies maintain stable (or rising) demand.

7. Exporting results

All main outputs are saved into /results/:

Role & level classification

Skill frequencies

Role × skill matrix

Top 3 skills per role

Monthly skill trends

KEY INSIGHTS

1. The job market is heavily cloud-driven

GCP, Snowflake, and Databricks appear across multiple roles — sometimes even more than Spark.

2. Engineering roles demand the broadest tech stack

Engineers dominate:

Spark

Kubernetes

GCP

Databricks

3. Analysts gravitate toward SQL-centric cloud tools

BigQuery + dbt + Snowflake form a strong analytics ecosystem.

4. Seniority often reflects orchestration skills

Tools like Airflow, Databricks, and Kafka appear more often in senior posts.

5. Cloud + modern data tooling is no longer optional

These tools appear consistently across months → long-term stability of demand.

TEHNOLOGIES USED

Python

Pandas (chunked processing)

Matplotlib

Jupyter Notebook

Text parsing & keyword detection

Time series grouping

Heatmap visualization

AUTHOR

Ana Stevanovic
Data Scientist / Data Analyst / ML Enthusiast
🇷🇸 Serbia / 🇳🇴 Norway
