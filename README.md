# NYC 311 Service Requests: Do Response Times Differ Across Neighborhoods?

## Central question
Do response and resolution times for the same type of 311 complaint differ across
NYC boroughs and neighborhoods, and what factors help explain the differences?

### Sub-questions
1. How long do requests take to close, by complaint type, agency, and area?
2. Do gaps between areas persist within the same complaint type and agency?
3. How do resolution times vary by month, year, and day of week?
4. What share of requests are still open, by area?
5. Are slower areas associated with neighborhood income or demographics?

## Dataset
- **Source:** [NYC Open Data: 311 Service Requests from 2020 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/about_data)
- **Original size:** approx. 22 million rows and 44 columns.
- **Data extracted on:** [add the date you downloaded it]

### Initial filtering
I used the query function on the NYC Open Data website to:
- Remove columns not relevant to the research question (11 columns kept).
- Keep requests created from **January 2023 to December 2025**. Requests from
  2020-2022 were excluded because of pandemic-related distortions, and 2026 was
  excluded because it is an incomplete year.

After these changes the dataset contains approx. 10 million rows and 11 columns.
Filtering was done on the created date, not the closed date.

## Tools
- Python (cleaning, statistics)
- SQL / DuckDB (analysis)
- Power BI (visualization)
- GitHub (version control)

## Project structure
- `data/`: raw and processed data (not tracked in Git because of file size)
- `scripts/`: Python scripts for conversion and cleaning
- `sql/`: SQL queries, one per sub-question
- `notebooks/`: exploratory notebooks
- `results/`: small aggregated result tables
- `visuals/`: dashboard and charts
- `report/`: final report and presentation

## Status
Work in progress.

## Limitations (to be completed)
