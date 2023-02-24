import requests
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime


class BybitFetch:
    def __init__(self):
        load_dotenv()
        self.endpoint = "https://api.bybit.com"
        self.headers

    def getFundingRateHistory(category, symbol):
        res = requests.get(
            (
                f"https://api.bybit.com/v5/market/funding/history?category={category}&symbol={symbol}"
            )
        )
        # print(res.text["result"])
        df = pd.DataFrame(pd.read_json(res.text)["result"][1])
        # df1 = pd.DataFrame(df)
        df["dateTime"] = pd.to_datetime(df["fundingRateTimestamp"], unit="ms")
        df.set_index("dateTime", inplace=True)
        return df


def main():
    BF = BybitFetch
    print(BF.getFundingRateHistory("inverse", "ETHPERP"))


if __name__ == "__main__":
    main()
