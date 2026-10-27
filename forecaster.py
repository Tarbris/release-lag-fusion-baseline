"""Editable starting forecaster; uses only target history, without exogenous fusion."""

class Forecaster:
    def predict(self, t, target_history, published_x):
        return float(target_history[-1]) if target_history else 0.0
