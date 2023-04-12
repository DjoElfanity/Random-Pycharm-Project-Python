from ibapi.client import EClient
from ibapi.common import TickerId, TickAttrib
from ibapi.ticktype import TickTypeEnum, TickType
from ibapi.wrapper import EWrapper

class OptionDataRequestor(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId:int, errorCode:int, errorString:str):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def tickPrice(self, reqId: TickerId, field: TickType, price: float, attrib: TickAttrib):
        if field == TickTypeEnum.DELTA:
            print("Delta: ", price)


class Stock:
    pass


def main():
    app = OptionDataRequestor()
    app.connect("127.0.0.1", 7497, 0)

    # Request option data for stock with symbol "AAPL"
    app.reqMktData(1, Stock("AAPL", "SMART", "USD"), "", False, False, [])

if __name__ == "__main__":
    main()