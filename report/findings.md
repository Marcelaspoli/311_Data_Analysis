Findings: NYC 311 Noise - Residential response times

Working notes, updated as the analysis goes. Everything here is about Noise - Residential complaints (handled by the NYPD) created between January 2023 and December 2025. Resolution time means the hours between the created date and the closed date. I use medians and 90th percentiles (p90) because waits are very skewed.

Data summary
1,139,683 requests. Cleaning removed 166 of them (closed before they were created, or took over 30 days to close), leaving 1,139,517.
Every request has a closed date, so there are no open cases to deal with.
288 rows have no borough and 317 have no valid zip code. They stay in the data but are left out of the geographic comparisons.
Q1. How long do requests take, by area?

By borough (requests, median wait, p90 wait):

Bronx: 427,583 requests, median 1.60 h, p90 11.15 h
Queens: 214,569 requests, median 0.90 h, p90 4.57 h
Staten Island: 28,642 requests, median 0.75 h, p90 2.52 h
Brooklyn: 283,527 requests, median 0.70 h, p90 3.07 h
Manhattan: 184,908 requests, median 0.63 h, p90 2.93 h

What stands out:

The Bronx waits about 2.5 times longer than Manhattan at the median and about 4 times longer at p90.
Bronx Community Board 12 alone has 210,457 requests, a 2.42 h median and a 14.77 h p90. Without it the Bronx median falls to 1.15 h and the p90 to 6.65 h, which is still the slowest borough.
The other Bronx boards in the top 10 slowest have medians of 1.35 to 1.95 h.
Records where the board and the borough don't match (for example "08 BRONX" labelled as Manhattan, 549 rows) are left out of the community board comparison.

Q2. Do the gaps persist?

The Bronx is the slowest borough in every year. Median wait by year:

2023: Bronx 1.00 h, Manhattan 0.48 h
2024: Bronx 1.80 h, Manhattan 0.63 h
2025: Bronx 1.77 h, Manhattan 0.90 h

More detail:

Bronx CB 12 had 9,729 requests in 2023, 69,779 in 2024 and 130,949 in 2025. The rest of the Bronx grew only about 20% (65,345 to 78,399), similar to Brooklyn and Manhattan.
CB 12 was already slower than the rest of the Bronx in quiet quarters (about 1.1 to 2.0 h versus 0.7 h from Q3 2023 to Q2 2024).
During the surge, waits did not simply follow volume. In Q4 2025 CB 12 had 64,846 requests with a 1.12 h median, while in Q4 2024 it had 43,115 requests with a 5.23 h median.
Nothing in this dataset explains why CB 12 volume surged. The cause is not established.
Q3. How do waits vary over time?
Baseline: from mid-2023 to spring 2024 monthly medians were about 0.5 to 0.7 h. January to April 2023 was slower (0.93 to 1.10 h), possibly because of a process change.
Wave 1 (Sep 2024 to Jan 2025): monthly requests rose from about 27,000 to 70,837 and the median from 0.83 h to 3.50 h in January 2025. Both fell back by February 2025.
Between the waves: medians recovered gradually to about 0.9 h by mid-2025, still above the 2023 baseline.
Wave 2 (from Oct 2025): requests reached 57,285 in December 2025 with a 1.45 h median. The data ends there.
Seasonality can't be separated from the 2024-25 surges with only one calm year.
Weekday (by creation date, all three years together): Saturday and Sunday make up 41% of requests (472,083 of 1,139,517), roughly twice the volume of a typical weekday, yet they have the shortest waits (median 0.83 h, p90 5.3 and 5.0 h). Monday and Tuesday have the longest tails (p90 7.73 and 8.95 h). Median differences between days are small (0.83 to 1.03 h).
Time of day: on Mondays, requests peak late in the evening but the longest waits are at 4 to 7 a.m. and 2 to 6 p.m. (about 1.3 to 1.4 h).
Early 2023 drop: between April and June 2023 the median fell by 45% to 68% in all five boroughs at once (Bronx 2.10 to 0.68 h, Manhattan 0.73 to 0.38 h). A drop that happens everywhere at the same time points to a citywide change, but the cause isn't in the data. January to April 2023 is treated as unrepresentative, and June 2023 to May 2024 is used as the calm baseline.
Borough by month: the Bronx was the slowest borough in every month from June 2024 to August 2025 (median 0.65 h in May 2024, 5.92 h in December 2024, 1.02 h in June 2025), but not in January to May 2024 (Queens slightly slower) or in September to November 2025 (Bronx at or below the other boroughs).
Citywide lengthening: comparing December 2023 with December 2025, medians grew 1.8 to 2.3 times in every borough (Brooklyn 0.58 to 1.20 h, Manhattan 0.47 to 0.98 h, Bronx 0.82 to 1.68 h). The volume surges are concentrated in Bronx CB 12, but the longer waits are not limited to the Bronx.

Wait time and outcome (links Q1 and Q4)

Share of requests closed as "no evidence" or "action taken", by how long the request waited:

Under 30 min: 338,975 requests, 34.4% no evidence, 36.0% action taken
30 to 60 min: 267,502 requests, 35.7% no evidence, 39.5% action taken
1 to 2 h: 202,156 requests, 41.4% no evidence, 31.6% action taken
2 to 4 h: 151,049 requests, 49.5% no evidence, 21.7% action taken
Over 4 h: 179,835 requests, 61.6% no evidence, 10.2% action taken

What this shows:

The longer the wait, the more often officers find no evidence and the less often action is taken.
The Bronx has 48.6% "no evidence" outcomes versus 35.4% in Brooklyn.
This is an association. It probably runs in both directions, since noise that stops on its own leaves nothing to find.
The pattern holds within every borough. For example, "no evidence" rises from 29.2% to 65.3% in Queens and from 37.9% to 63.9% in the Bronx as waits grow from under 30 minutes to over 4 hours.
The Bronx's higher overall share of "no evidence" is mostly explained by 28.5% of its requests waiting over 4 hours, versus 6% to 12% in Queens, Brooklyn and Manhattan (and 3.9% in Staten Island).
Even for responses under 30 minutes, action is taken less often in the Bronx (26.2%, versus 31% to 56% elsewhere).
Q4. What does a closed case mean?

Closed means the police responded and closed the ticket. It doesn't mean the noise was resolved.

Roughly 38% of requests closed with "no evidence of the violation".
Roughly 30% closed with action taken to fix the condition.
About 11.5% closed as police action not necessary, 8% because officers couldn't get in, and 1.3% because those responsible were gone when officers arrived.
Median waits differ by outcome: 0.67 h when action was taken, 1.22 h for "no evidence", and 1.50 h when those responsible were gone.

So resolution time here measures the time until a police response, not the time until the problem was fixed.

Q5. Income and demographics

Median household income by zip code (ACS 2020-2024 5-year, table B19013) was joined to the median wait for each zip. Zips with fewer than 300 requests were left out, and so were two zips with the capped income of $250,001, which leaves 166 zips. I ran it for all data, without Bronx CB 12, and for a calm baseline (June 2023 to May 2024).

Citywide there is a weak negative association between income and wait (Spearman -0.34, about 4% shorter median wait per extra $10,000, R-squared 0.13). In the baseline it is weaker (-0.22, 2.7% per $10,000, R-squared 0.06).
By income quartile, the highest-income quartile waits roughly 30% less (0.58 h) than the other three (0.80 to 0.88 h, without CB 12). The lowest-income quartile is not the slowest. The all-data Q2 median (1.27 h, p90 9.97 h) is inflated by the CB 12 zips.
Within boroughs the relationship isn't consistent. In the Bronx, higher-income zips have longer waits (rho +0.60 to +0.72 in every scenario). Queens and Manhattan are negative in some scenarios but not all, and Brooklyn and Staten Island are mostly not significant. A lot of the citywide association comes from differences between boroughs, since the Bronx is both lower-income and slower.
Conclusion: income is at most a modest factor. Borough and the CB 12 surges matter more. These are associations between areas, not causes, and they say nothing about individual callers.
Regression: which factors explain the differences?

I regressed log wait time on borough, income and time controls. Part A works at zip level (166 zips). Part B uses a fixed sample of 199,739 requests (about 18% of the data), with standard errors clustered by zip. Percentages describe typical waits (geometric means).

Income mostly disappears once borough is included. At zip level the income effect falls from -4.1% per $10,000 to -1.6% (CI -3.3% to +0.1%), and in the baseline period from -2.7% to -0.2%. Adjusted R-squared rises from 0.13 to 0.31.
Borough gaps persist after controlling for year, month, weekday, hour and income. With Manhattan as the reference: Bronx +84.5% (CI +47% to +131%), Queens +50.8% (CI +27% to +80%), Staten Island +19.1% (CI +5% to +36%), Brooklyn +9.4% (not significant).
Bronx CB 12 accounts for part of the Bronx gap. With a CB 12 indicator the Bronx falls to +53.7% (CI +18% to +101%) and CB 12 adds +42.9% on top (CI +14% to +80%). That means requests in CB 12 wait about 2.2 times as long as comparable Manhattan requests, versus about 1.5 times for the rest of the Bronx. Queens stays at about +50%.
The models explain little of the variation in individual waits (R-squared 0.11 to 0.12), so most of it comes from factors that aren't in this dataset.
Each borough coefficient averages three years, although the Bronx gap changed over time. Results are associations, not causes.

Limitations

Complaint volume reflects who chooses to report, not where noise actually happens.
"Closed" means a police response, not a resolution.
Results cover one complaint type and may not apply to other 311 services.
Associations only. The data can't show causes.
The 2024-25 surges are unexplained by this dataset.

Still to do

Tableau dashboard, report and presentation.