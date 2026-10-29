Findings: NYC 311 Noise - Residential Response Times

Working notes, updated as the analysis progresses. All results use Noise - Residential complaints (NYPD), created January 2023 to December 2025. "Resolution time" means hours from created date to closed date. Medians and 90th percentiles (p90) are used because durations are heavily skewed.

Data summary

    1,139,683 requests; 166 removed in cleaning (closed before created, or over 30 days to close), leaving 1,139,517.
    Every request has a closed date, so there are no open cases to handle.
    288 rows have no borough and 317 have no valid zip. They are kept but excluded from geographic comparisons.


Q1. How long do requests take, by area?

Borough	Requests	Median (h)	p90 (h)
Bronx	427,583	1.60	11.15
Queens	214,569	0.90	4.57
Staten Island	28,642	0.75	2.52
Brooklyn	283,527	0.70	3.07
Manhattan	184,908	0.63	2.93

    The Bronx waits about 2.5 times longer than Manhattan at the median, and about 4 times longer at p90.

    Bronx Community Board 12 alone has 210,457 requests, a 2.42 h median and a 14.77 h p90. Without it, the Bronx median falls to 1.15 h and p90 to 6.65 h, still the slowest borough.
    Other Bronx boards in the top 10 slowest have medians of 1.35 to 1.95 h.

    Records where the board and borough do not match (for example "08 BRONX" labelled as Manhattan, 549 rows) are excluded from the community board comparison.

Q2. Do the gaps persist?

The Bronx is the slowest borough in every year (median hours):

Year	Bronx	Manhattan
2023	1.00	0.48
2024	1.80	0.63
2025	1.77	0.90

    Bronx CB 12 requests: 9,729 (2023), 69,779 (2024), 130,949 (2025). The rest of the Bronx grew only about 20% (65,345 to 78,399), similar to Brooklyn and Manhattan.

    CB 12 was already slower than the rest of the Bronx in quiet quarters (about 1.1 to 2.0 h versus 0.7 h from Q3 2023 to Q2 2024).

    Within the surge, waits did not simply follow volume. In Q4 2025 CB 12 had 64,846 requests with a 1.12 h median, while in Q4 2024 it had 43,115 requests with a 5.23 h median.

    Nothing in this dataset explains why CB 12 volume surged. The cause is not established.

Q3. Variation over time

Baseline: 
    from mid-2023 to spring 2024 monthly medians were about 0.5 to 0.7 h. January to April 2023 was slower (0.93 to 1.10 h), possibly a process change.
Wave 1 (Sep 2024 to Jan 2025): 
    monthly requests rose from about 27,000 to 70,837 and the median from 0.83 h to 3.50 h in January 2025. Both fell back by February 2025.
Between waves: 
    medians recovered gradually to about 0.9 h by mid-2025, still above the 2023 baseline.
Wave 2 (from Oct 2025): 
    requests reached 57,285 in December 2025 with a 1.45 h median. The data ends there. Seasonality cannot be separated from the 2024-25 surges with only one calm year.
Weekday (by creation date, all three years pooled): 
    Saturday and Sunday account for 41% of requests (472,083 of 1,139,517), roughly twice the volume of a typical weekday, yet have the shortest waits (median 0.83 h, p90 5.3 and 5.0 h). Monday and Tuesday have the longest tails (p90 7.73 and 8.95 h). Median differences between days are small (0.83 to 1.03 h).
Time of day:
     on Mondays, requests peak late evening but the longest waits are at 4 to 7 a.m. and 2 to 6 p.m. (about 1.3 to 1.4 h).
-Early-2023 drop:
    between April and June 2023 the median fell by 45% to 68% in all five boroughs at once (Bronx 2.10 to 0.68 h, Manhattan 0.73 to 0.38 h). A simultaneous drop points to a citywide change rather than a local one; the cause is not in the data. January to April 2023 is treated as unrepresentative, and June 2023 to May 2024 is used as the calm baseline.
Borough by month:
    the Bronx was the slowest borough in every month from June 2024 to August 2025 (median 0.65 h in May 2024, 5.92 h in December 2024, 1.02 h in June 2025), but not in January to May 2024 (Queens slightly slower) or September to November 2025 (Bronx at or below other boroughs).
Citywide lengthening:
    comparing December 2023 with December 2025, medians grew 1.8 to 2.3 times in every borough (Brooklyn 0.58 to 1.20 h, Manhattan 0.47 to 0.98 h, Bronx 0.82 to 1.68 h). The volume surges are concentrated in Bronx CB 12, but the lengthening of waits is not limited to the Bronx.

Wait time and outcome (links Q1 and Q4)

Wait	Requests	"No evidence"	Action taken
under 30 min	338,975	34.4%	36.0%
30-60 min	267,502	35.7%	39.5%
1-2 h	202,156	41.4%	31.6%
2-4 h	151,049	49.5%	21.7%
over 4 h	179,835	61.6%	10.2%

    The longer the wait, the more often officers find no evidence and the less often action is taken.

    The Bronx has 48.6% "no evidence" outcomes versus 35.4% in Brooklyn.

    This is an association. It likely runs in both directions (noise that stops on its own leaves nothing to find). 

    Query 10 confirms the pattern holds within every borough (for example, "no evidence" rises from 29.2% to 65.3% in Queens and from 37.9% to 63.9% in the Bronx as waits grow from under 30 min to over 4 h). The Bronx's higher overall share of "no evidence" outcomes (48.6%) is mostly explained by 28.5% of its requests waiting over 4 hours, versus 6% to 12% in other boroughs (except Staten Island at 3.9%). Even for responses under 30 minutes, action is taken less often in the Bronx (26.2%, versus 31% to 56% elsewhere).

Q4. What does a closed case mean?

    Closed means the police responded and closed the ticket, not that the noise was resolved.

    Roughly 38% of requests closed with "no evidence of the violation".
    Roughly 30% closed with action taken to fix the condition.
    About 11.5% closed as police action not necessary, 8% because officers could not gain entry, and 1.3% because those responsible were gone on arrival.
    Median waits differ by outcome: 0.67 h when action was taken, 1.22 h for "no evidence", 1.50 h when those responsible were gone.

    So resolution time here measures time until a police response, not time until the problem was fixed

Q5. Income and demographics

    Median household income by zip code (ACS 2020-2024 5-year, table B19013) was joined to zip-level median resolution times (zips with 300+ requests, excluding two zips with the capped income of $250,001; 166 zips in total). Run for all data, without Bronx CB 12, and for a calm baseline (Jun 2023 to May 2024).

    - Citywide: weak negative association between income and wait (Spearman -0.34; about 4% shorter median wait per extra $10,000; R-squared 0.13). In the baseline it is weaker (-0.22; 2.7% per $10,000; R-squared 0.06).
    - By income quartile: the highest-income quartile waits roughly 30% less (0.58 h) than the other three (0.80 to 0.88 h, excluding CB 12). The lowest-income quartile is not the slowest. The all-data Q2 median (1.27 h, p90 9.97 h) is inflated by the CB 12 zips.
    - Within boroughs: the relationship is not consistent. In the Bronx higher-income zips have longer waits (rho +0.60 to +0.72 in every scenario). Queens and Manhattan show negative values in some scenarios but not all, and Brooklyn and Staten Island are mostly not significant. Much of the citywide association therefore reflects between-borough differences, since the Bronx is both lower-income and slower.
    - Conclusion: income is at most a modest factor in response-time differences. Borough and the CB 12 surges matter more. Results are area-level associations, not causes, and say nothing about individual callers.

Limitations

Complaint volume reflects who chooses to report, not where noise actually occurs.
"Closed" means a police response, not a resolution.
Results cover one complaint type and may not apply to other 311 services.
Associations only; the data cannot show causes.
The 2024-25 surges are unexplained by this dataset.

Still to do

Tableau dashboard, report, presentation.