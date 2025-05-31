import yfinance as yf

class YahooRiskFreeRateProvider:
    """
    Retrieves risk-free rate proxy from Yahoo Finance.
    Typically uses the 13-week Treasury Bill (^IRX) as a short-term proxy.
    """

    def __init__(self):
        self.ticker = "^IRX"  # 13-week Treasury bill

    def get_rate(self) -> float:
        """
        Returns annualized risk-free rate as a decimal (e.g., 0.045 = 4.5%)
        Yahoo Finance returns the 13-week T-bill rate as an APR percentage.

        We'll convert the 13-week rate to annualized using simple compounding.
        """
        tbill = yf.Ticker(self.ticker)
        hist = tbill.history(period="1d")
        latest_rate = hist["Close"].iloc[-1] / 100  # convert from percent to decimal

        # Annualize the 13-week rate:
        annualized_rate = (1 + latest_rate) ** (52/13) - 1
        return annualized_rate
