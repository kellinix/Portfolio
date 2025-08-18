A/B Test Deep-Dive — Conversion Uplift (Variant B vs Control A)

1) Project Brief

Goal: Determine whether the new website design (Variant B) improves conversion vs the current design (Control A).
Primary Metric: Conversion rate (purchases / users).
Audience: Product managers, Growth/Marketing, Leadership.

2) Experiment Design

Population: 10,000 users randomly split 50/50 into A and B.
Test Window: Rolling dates between 2025-07-19 and 2025-08-19.
Assignment: Equal probability to A or B at first visit.
Success Criterion: Statistically significant lift in conversion at α = 0.05 (two-sided).

3) Data & SQL Summary

Table: ab_test (user_id, group, converted, country, device, timestamp)

Overall conversion (from SQL):
A (control): 5,076 users → 519 conversions → 10.22%
B (variant): 4,924 users → 622 conversions → 12.63%
Observed absolute lift: +2.41 pp
Observed relative lift: +23.6%

Sanity checks (from SQL):
By device: B > A across desktop, mobile, tablet (~12.3–12.8% vs ~10.2%).
By country: B > A across CA, DE, FR, UK, US.
By day: Both groups present throughout; natural daily noise, no exposure gaps.

4) Hypothesis Test (Python)

Null (H₀): p_A = p_B
Alt (H₁): p_A ≠ p_B

Results (two-proportion z-test):
Z: −3.786
p-value: 0.0002 → Reject H₀ at α = 0.05
95% CIs:
A: 10.22% (9.39%–11.06%)
B: 12.63% (11.70%–13.56%)

Conclusion: Variant B’s conversion rate is significantly higher than A’s.

5) Visual Evidence

Bar chart with 95% CI: shows clear separation (B above A).
Daily trend: B generally above A across the test window (expected random fluctuations).

6) Decision & Recommendation

Decision: Ship Variant B to 100% of traffic.
Rationale: Statistically significant +23.6% relative lift in conversion; consistent across devices and countries.

7) Business Impact (Back-of-Envelope)

If your site receives N users/month and baseline conversion is 10.22%, moving to 12.63% yields:

Δ conversions/month ≈ N × (0.1263 − 0.1022) = N × 0.0241

With an average order value AOV, Δ revenue ≈ N × 0.0241 × AOV.
(Swap in your actual traffic and AOV to quantify impact.)

8) Risks, Assumptions, and Guardrails

Randomization: Assumed unbiased; SQL device/country checks support this.

Duration/Seasonality: ~1 month; if seasonality exists, consider a longer follow-up.

Novelty effects: Monitor post-launch in case effects decay.

Multiple looks / peeking: Results reported at the end of the test (no sequential stopping).

9) Next Steps

Post-launch monitoring: Track conversion and downstream metrics (AOV, retention).

Segment deep-dives: Explore outsized lift in DE/UK; tailor creatives if helpful.

Experiment 2: Test targeted enhancements to mobile checkout to compound gains.

Power BI (optional): Build a simple A/B monitoring dashboard (conversion, CI, daily trend).