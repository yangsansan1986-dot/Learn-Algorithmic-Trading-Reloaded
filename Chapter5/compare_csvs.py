import pandas as pd

basic_mr = pd.read_csv('basic_trend_following.csv')
vol_mr = pd.read_csv('volatility_adjusted_trend_following.csv')

import matplotlib.pyplot as plt

basic_mr['Pnl'].plot(x='Date', color='b', lw=1., label='Basic Trend Following Pnl', legend=True)
vol_mr['Pnl'].plot(x='Date', color='g', lw=1., label='Volatility Adjusted Trend Following Pnl', legend=True)
plt.show()
