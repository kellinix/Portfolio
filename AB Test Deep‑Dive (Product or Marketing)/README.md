
# A/B Test Deep-Dive: Conversion Uplift Analysis

## Overview

This project analyzes the impact of a new website design (Variant B) on user conversion rates compared to the current design (Control A). It combines SQL data exploration, statistical hypothesis testing in Python, and visualizations to deliver actionable insights.

## Project Structure

- `data/`
	- `ab_test.csv`: Raw experiment data.
	- `data.py`: Data processing script.
	- `processed/ab_test.db`: SQLite database for analysis.
- `sql/`
	- SQL scripts for extracting and summarizing experiment results (`total_users_per_group.sql`, `conversions_per_group.sql`, `daily_trend.sql`, `breakdown_by_device.sql`).
- `notebook/`
	- `visual.py`: Python script for generating conversion rate and daily trend visualizations.
	- `hypothesis.py`: Statistical analysis and hypothesis testing.
	- `conversion_rates_with_CI.png`, `daily_conversion_trends.png`: Output charts.
- `docs/`
	- `ab_test_case_study.md`: Full case study and business impact summary.
	- `result.md`: Statistical test results and interpretation.
	- `sql_results.md`: SQL analysis breakdown.

## Setup

### Prerequisites

- Python 3.8+
- Required Python libraries: `pandas`, `numpy`, `scipy`, `matplotlib`, `statsmodels`
- SQLite (or compatible SQL database)

### Installation

Clone the repository:
```sh
git clone <repo_url>
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

1. **SQL Analysis**  
	 Run SQL scripts in the `sql/` folder against `data/processed/ab_test.db` to extract summary statistics and breakdowns.

2. **Statistical Testing**  
	 Use `notebook/hypothesis.py` to perform two-proportion z-tests and calculate confidence intervals.

3. **Visualization**  
	 Run `notebook/visual.py` to generate bar charts and daily conversion trends.

## Results

- **Conversion Rates:**  
	- Control (A): 10.22% (95% CI: 9.39%–11.06%)
	- Variant (B): 12.63% (95% CI: 11.70%–13.56%)
	- Absolute lift: +2.41 percentage points
	- Relative lift: +23.6%
- **Statistical Significance:**  
	- Z-statistic: -3.786  
	- p-value: 0.0002 (significant at α = 0.05)
- **Visuals:**  
	- Bar chart and daily trend plots show consistent uplift for Variant B.

## Business Impact

Rolling out Variant B is expected to drive a ~24% increase in conversions. See `docs/ab_test_case_study.md` for a detailed impact analysis and recommendations.

## License

MIT License