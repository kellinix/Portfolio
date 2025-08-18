# H₀ (null): Conversion rate of A = Conversion rate of B
# H₁ (alt): Conversion rate of A ≠ Conversion rate of B

import numpy as np
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

# Data from SQL
conversions = np.array([519, 622])   # conversions in A, B
totals = np.array([5076, 4924])      # total users in A, B

# Two-sided z-test
z_stat, p_value = proportions_ztest(conversions, totals)
(lower_a, upper_a) = proportion_confint(conversions[0], totals[0], method='normal')
(lower_b, upper_b) = proportion_confint(conversions[1], totals[1], method='normal')

print(f"Z-statistic: {z_stat:.3f}")
print(f"P-value: {p_value:.4f}")
print(f"Conversion rate A: {conversions[0]/totals[0]:.4%} (95% CI: {lower_a:.4%}–{upper_a:.4%})")
print(f"Conversion rate B: {conversions[1]/totals[1]:.4%} (95% CI: {lower_b:.4%}–{upper_b:.4%})")
