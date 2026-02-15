import pymc as pm
import numpy as np
import arviz as az

def run_change_point_model(returns: np.ndarray):
    n = len(returns)

    with pm.Model() as model:
        tau = pm.DiscreteUniform("tau", lower=0, upper=n - 1)

        mu_1 = pm.Normal("mu_1", mu=0, sigma=1)
        mu_2 = pm.Normal("mu_2", mu=0, sigma=1)

        sigma = pm.Exponential("sigma", 1)

        mu = pm.math.switch(np.arange(n) < tau, mu_1, mu_2)

        pm.Normal("obs", mu=mu, sigma=sigma, observed=returns)

        trace = pm.sample(return_inferencedata=True)

    return model, trace
