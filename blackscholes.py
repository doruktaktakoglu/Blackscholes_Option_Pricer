from math import log, sqrt, exp
from scipy.stats import norm
from models import BlackScholesInput

class BlackScholesPricer:
    def __init__(self, data: BlackScholesInput):
        self.S = data.S
        self.K = data.K
        self.T = data.T
        self.r = data.r
        self.sigma = data.sigma
        self.option_type = data.option_type

        self.d1 = (log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * sqrt(self.T))
        self.d2 = self.d1 - self.sigma * sqrt(self.T)

    def price(self) -> float:
        if self.option_type == 'call':
            return self.S * norm.cdf(self.d1) - self.K * exp(-self.r * self.T) * norm.cdf(self.d2)
        else:  # put
            return self.K * exp(-self.r * self.T) * norm.cdf(-self.d2) - self.S * norm.cdf(-self.d1)
