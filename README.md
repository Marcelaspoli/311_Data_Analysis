# NYC 311 Service Requests: Do Response Times Differ Across Neighborhoods?

## Central question
Do response and resolution times for the same type of 311 complaint differ across NYC boroughs and neighborhoods, and what factors help explain the differences?

This project focuses on one complaint type, **Noise - Residential** (NYPD), so that areas are compared like with like.

### Sub-questions
1. How long do requests take to close, by area (borough and community board)?
2. Do gaps between areas persist within the same complaint type and agency, and across time?
3. How do resolution times vary by month, year, and day of week?
4. What does "closed" mean? 
5. Are slower areas associated with neighborhood income or demographics?

## Dataset
- **Source:** [NYC Open Data: 311 Service Requests from 2020 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/about_data)
- **Original size:** approx. 22 million rows and 44 columns.
- **Data extracted on:** 09 Oct 2026
- **Income data:** median household income by ZIP Code Tabulation Area (table B19013) from the [US Census Bureau American Community Survey](https://data.census.gov), 2020-2024 5-year estimates, downloaded with `scripts/05_download_census.py` (requires a free Census API key).

### Initial filtering
I used the query function on the NYC Open Data website to:
- Remove columns not relevant to the research question (11 columns kept).
- Keep requests created from **January 2023 to December 2025**. Requests from
  2020-2022 were excluded because of pandemic-related distortions, and 2026 was
  excluded because it is an incomplete year.

After these changes the dataset contains approx. 10 million rows and 11 columns.

## Tools
- Python (cleaning, statistics)
- SQL / DuckDB (analysis)
  * DuckDB because the analysis is single-user and runs locally on a laptop
- Tableau Public (visualization)
- GitHub (version control)

## Project structure
- `data/`: raw and processed data (not tracked in Git because of file size)
- `scripts/`: Python scripts for conversion, cleaning and running SQL
- `sql/`: SQL queries, one per sub-question
- `notebooks/`: exploratory notebooks
- `results/`: small aggregated result tables
- `visuals/`: dashboard and charts
- `report/`: final report and presentation

## Status
Data cleaned; SQL analysis in progress.

## Limitations (to be completed)
- Complaint volume reflects who chooses to report, not necessarily where problems exist.
- "Closed" does not always mean "resolved" (sub-question 4).
- Findings describe associations not causes.
- Results cover one complaint type, so they may not apply to other 311 services.