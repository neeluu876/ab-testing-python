# A/B Testing in Python

I first analyzed A/B tests in Excel during a career accelerator program. This repo redoes them
in Python and goes further: power analysis, confidence intervals, and a simulation of how
often a test misleads you.

## What's here
- `src/ab_tools.py`: a two-proportion z-test with confidence interval, and a sample-size calculator
- `tests/`: unit tests for those functions
- `notebooks/`: the H&M email and Warby Parker landing page analyses redone in Python (TODO)

## Progress checklist
- [ ] Redo the H&M email subject-line test in Python
- [ ] Redo the Warby Parker landing page test
- [ ] Add a simulation: run many fake A/A tests and count false positives at alpha = 0.05
- [ ] Design and analyze one new test of my own, with hypotheses and confounders

## What I learned
(Fill in as you go.)
