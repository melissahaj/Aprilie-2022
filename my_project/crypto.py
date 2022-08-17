class Crypto:
    def init(self, ticker: str, company: str, ammount: float):
        self.ticker = ticker
        self.company = company
        self.ammount = ammount

    def to_json(self) -> dict:
        return {
            "ticker": self.ticker,
            "company": self.company,
            "amount": self.amount,
        }
