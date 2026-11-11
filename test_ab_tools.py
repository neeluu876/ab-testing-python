import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from ab_tools import sample_size_per_group, two_proportion_ztest


def test_ztest_detects_clear_difference():
    r = two_proportion_ztest(100, 1000, 130, 1000)
    assert abs(r["difference"] - 0.03) < 1e-9
    assert 2.0 < r["z"] < 2.2
    assert r["p_value"] < 0.05
    assert r["ci"][0] < r["difference"] < r["ci"][1]


def test_ztest_no_difference():
    r = two_proportion_ztest(100, 1000, 100, 1000)
    assert r["z"] == 0
    assert r["p_value"] > 0.99


def test_sample_size_matches_known_value():
    # Standard result: 10% -> 12%, alpha 0.05, power 0.8 needs about 3,800 per group.
    n = sample_size_per_group(0.10, 0.12)
    assert 3700 <= n <= 3950
