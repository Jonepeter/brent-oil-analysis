# Methodology

## Bayesian Change Point Detection

### Model Specification
The analysis uses a single change point model where the time series switches between two regimes:

```
τ ~ DiscreteUniform(1, n-2)
μ₁, μ₂ ~ Normal(0, 1)
σ₁, σ₂ ~ HalfNormal(1)
y_t ~ Normal(μ_switch, σ_switch)
```

### Data Preprocessing
1. **Log Transformation**: Convert prices to log returns for stationarity
2. **Outlier Detection**: Identify extreme observations using z-scores
3. **Stationarity Testing**: Augmented Dickey-Fuller test validation

### Sampling Strategy
- **MCMC Chains**: 2 parallel chains
- **Samples**: 2000 draws per chain
- **Tuning**: 1000 warm-up samples
- **Convergence**: R-hat < 1.1 diagnostic

### Event Correlation
Change points are correlated with geopolitical events within 30-60 day windows to assess causal relationships.