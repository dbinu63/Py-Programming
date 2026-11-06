# create trade class (ABC) with trade_id and country props, abstractmethod show_trade()
# import class - goods and value (usd) props, export class - shipping, material props, value props

from abc import ABC, abstractmethod


class Trade(ABC):
    def __init__(self, trade_id, country):
        self.trade_id = trade_id
        self.country = country

    @abstractmethod
    def show_trade(self):
        pass


class Import(Trade):
    def __init__(self, trade_id, country, goods, value):
        super().__init__(trade_id, country)
        self.goods = goods
        self.value = value

    def show_trade(self):
        print(f"Trade ID: {self.trade_id}")
        print(f"Country: {self.country}")
        print(f"Goods: {self.goods}")
        print(f"Value (USD): ${self.value}")


class Export(Trade):
    def __init__(self, trade_id, country, shipping, material, value):
        super().__init__(trade_id, country)
        self.shipping = shipping
        self.material = material
        self.value = value

    def show_trade(self):
        print(f"Trade ID: {self.trade_id}")
        print(f"Country: {self.country}")
        print(f"Shipping: {self.shipping}")
        print(f"Material: {self.material}")
        print(f"Value (USD): ${self.value}")


def main():
    import_trade = Import(
        "IMP001",
        "Japan",
        "Electronics",
        50000
    )

    export_trade = Export(
        "EXP001",
        "Canada",
        "Air Freight",
        "Steel",
        75000
    )

    import_trade.show_trade()
    print()
    export_trade.show_trade()


if __name__ == "__main__":
    main()
