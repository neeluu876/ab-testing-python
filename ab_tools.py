"""Small, dependency-free helpers for analyzing A/B tests on conversion rates."""
from math import ceil, sqrt
from statistics import NormalDist

_N = NormalDist()


def two_proportion_ztest(x1, n1, x2, n2, alpha=0.05):
    """Two-sided z-test comparing control (x1 of n1) with test (x2 of n2).

    Returns the two rates, their difference (test minus control), the z statistic,
    the p-value, and a confidence interval for the difference.
    """
    if min(n1, n2) <= 0:
        raise ValueError("Group sizes must be positive.")
    p1, p2 = x1 / n1, x2 / n2
    pooled = (x1 + x2) / (n1 + n2)
    se_pooled = sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    z = (p2 - p1) / se_pooled
    p_value = 2 * (1 - _N.cdf(abs(z)))
    se_diff = sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    z_crit = _N.inv_cdf(1 - alpha / 2)
    diff = p2 - p1
    return {
        "control_rate": p1,
        "test_rate": p2,
        "difference": diff,
        "z": z,
        "p_value": p_value,
        "ci": (diff - z_crit * se_diff, diff + z_crit * se_diff),
    }


def sample_size_per_group(p1, p2, alpha=0.05, power=0.8):
    """Sample size per group needed to detect a change from rate p1 to p2."""
    if p1 == p2:
        raise ValueError("Rates must differ.")
    z_a = _N.inv_cdf(1 - alpha / 2)
    z_b = _N.inv_cdf(power)
    p_bar = (p1 + p2) / 2
    numerator = (
        z_a * sqrt(2 * p_bar * (1 - p_bar))
        + z_b * sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    ) ** 2
    return ceil(numerator / (p1 - p2) ** 2)
