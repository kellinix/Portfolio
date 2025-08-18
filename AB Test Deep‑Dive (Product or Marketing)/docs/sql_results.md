A/B Test SQL Exploration Results

1. Overall Conversion

Group A (control): 5076 users → 519 conversions → 10.22% conversion rate
Group B (variant): 4924 users → 622 conversions → 12.63% conversion rate
Initial results suggest Group B outperforms Group A by ~2.4 percentage points, which is a relative lift of ~23.6%.

2. Device Breakdown

Conversion rates are consistent across devices within each group.

Group B is higher across desktop (12.8%), mobile (12.3%), tablet (12.8%) compared to Group A (~10.2% on all).
Device does not appear to bias results.

3. Country Breakdown

Group B outperforms Group A in every country.

Lift is strongest in Germany (13.7% vs 10.4%) and UK (12.6% vs 9.8%).
Even in US, where base rates are lower, Group B shows improvement (11.3% vs 9.2%).
Variant effect appears geographically consistent.

4. Daily Trend

Conversion rates fluctuate day-to-day, but no systematic data collection issues observed.
Both groups were exposed consistently across the test period.
Group B shows higher conversion most days, though with natural random variation.

SQL Summary
Group B (variant) consistently outperforms Group A (control) across overall results, device types, and countries.
Observed lift ≈ 2.4 percentage points → could be statistically significant, but needs validation with hypothesis testing (Python).