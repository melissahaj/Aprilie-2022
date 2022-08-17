import json
from crypto import Crypto


class CryptoRepository:
    def init(self):
        self.cryptos = {}
        self.load()

    def load(self):
        file = open("database.txt")
        json_items = file.read()
        file.close()
        items = json.loads(json_items)
        for one_item in items:
            new_crypto = Crypto(
                one_item["ticker"],
                one_item["company"],
                one_item["amount"],
            )
            self.cryptos[one_item["ticker"]] = new_crypto

    def add(self, new_crypto: Crypto):
        self.cryptos[new_crypto.ticker] = new_crypto
        self.save()

    def get_all(self) -> list[Crypto]:
        return self.cryptos.values()

    def remove(self, crypto_id: str):
        self.cryptos.pop(crypto_id)
        self.save()

    def save(self):
        list_json = json.dumps([x.to_json() for x in self.cryptos.values()])
        file = open("database.txt", "w")
        file.write(list_json)
        file.close()