# regime-stat-lab

**Multi-asset and multi timeframe return profiling (SPX, BTC, gold, FX) for regime analysis, Hurst/entropy, hypothesis testing, and trading edge exploration.**

### What is Hurst/Entropy Analysis?
- **Hurst Exponent (H)**: Measures trend persistence (H>0.5 = trending, H<0.5 = mean-reverting, H=0.5 = random walk)
- **Entropy**: Quantifies regime complexity/uncertainty 
- **Combined**: Identifies tradable market states across assets/timeframes

## Purpose
- Average return lookups for any date/window  
- Cross-asset regime comparison (trending vs mean-reverting)
- Hypothesis testing for trading edge development

## Current Data Quality (v3.0 - Jan 18 2026)
| Asset   | Calendar Days | API Days | Coverage | Notes          |
|---------|---------------|----------|----------|----------------|
| SP500   | 731           | 501      | 68%      | weekends normal|
| BTC     | 731           | 731      | 100%     | 24/7 trading   |
| NASDAQ  | 731           | 501      | 68%      | weekends normal|

## Key Insight
**APIs lie by omission** - yfinance skips weekends silently. v3.0 forces calendar comparison.

### Pipeline Vision
Clean CSVs → BigQuery → dbt transformations → Evidence dashboards