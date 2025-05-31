from models import BlackScholesInput
from blackscholes import BlackScholesPricer

if __name__ == "__main__":
    input_data = BlackScholesInput(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2,
        option_type='call'
    )

    pricer = BlackScholesPricer(input_data)
    price = pricer.price()
    print(f"Option Price: {price:.4f}")
