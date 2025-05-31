from models import BlackScholesInput
from blackscholes import BlackScholesPricer
from rates import YahooRiskFreeRateProvider

if __name__ == "__main__":
    rate_provider = YahooRiskFreeRateProvider()
    input_data = BlackScholesInput(
        S=100,
        K=100,
        T=1,
        r=rate_provider.get_rate(),
        sigma=0.2,
        option_type='call'
    )

    pricer = BlackScholesPricer(input_data)
    price = pricer.price()
    print(f"Option Price: {price:.4f}")
