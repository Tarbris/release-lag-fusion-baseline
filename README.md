# Release-lag exogenous forecast workspace

Edit only `forecaster.py`. Implement `Forecaster.predict(t, target_history,
published_x) -> finite float`. At decision time `t`, `target_history` has only
`y[0:t]`; `published_x` contains only `x[0:t-1]`, ending at `x[t-2]` because
each exogenous value arrives two rounds after its timestamp. The call returns
a forecast for `y[t]` before it is revealed. `t` runs from 2 through 1199;
rounds 2–39 initialize the forecaster and are excluded from score.

The synthetic target depends on its recent past and on a delayed, noisy
exogenous channel. The relationship can change at 300-round boundaries. The
environment does not disclose future `x`, future `y`, latent coefficients,
episode seeds, or evaluator code. Hidden mean squared error (MSE) across all
scored rounds is lower-is-better. Python 3.12 standard library; no network.
The weak starter is target persistence and ignores the published channel.
