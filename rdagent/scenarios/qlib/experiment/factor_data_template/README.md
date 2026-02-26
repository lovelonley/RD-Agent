# How to read files.
For example, if you want to read `filename.h5`
```Python
import pandas as pd
df = pd.read_hdf("filename.h5", key="data")
```
NOTE: **key is always "data" for all hdf5 files **.

# Here is a short description about the data

| Filename       | Description                                                      |
| -------------- | -----------------------------------------------------------------|
| "daily_pv.h5"  | Adjusted daily price and volume data.                            |


# For different data, We have some basic knowledge for them

## Feature Descriptions
| Field | Description |
| --- | --- |
| $open, $close, $high, $low, $volume, $vwap | Basic OHLCV and volume-weighted average price. |
| $change, $factor, $turnover_rate | Return, adjustment factor, and market liquidity (turnover). |
| $pe, $pb, $ps | Valuation multiples: Price-to-Earnings, Price-to-Book, Price-to-Sales. |
| $total_mv, $circ_mv | Size indicators: Total Market Value and Circulating Market Value. |
| $industry | Industry classification (SW 1st level coding). |
| $roe, $netprofit_yoy, $debt_ratio | Fundamentals: Return on Equity, Net Profit Growth (YoY), and Leverage Ratio. |
| $grossprofit_margin, $eps, $current_ratio | Efficiency/Profitability: Gross Margin, Earnings Per Share, and Liquidity. |
| $or_yoy, $q_roe, $op_yoy | Growth/Results: Operating Revenue Growth, Quarterly ROE, and Operating Profit Growth. |
| $bps, $ocfps | Asset/Cash: Book Value Per Share and Operating Cash Flow Per Share. |
| $north_money, $rzye | Capital Flows: Northbound Money and Margin Balance (RZY). |
| $net_mf_amount, $large_net_mf, $elg_net_mf | Money Flow: Total Net Inflow, Large Order Inflow, and Extra-large Order Inflow. |
| $net_mf_amount_ma5 | Sentiment: 5-day moving average of net money flow. |