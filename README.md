# Statistical-Arbitrage
Python Algorithm for Basic Stat Arbitrage trading in Forex through the MetaTrader 5 platform:
Just a little draft that I was working on during my mid year holidays, made with intermediate python skills in data science.
Please replace the login, password, and server variables with the values corresponding to your login details.
Note, this code was partly edited by AI, as I only have intermediate skills in Python.
The way it works:
- Connects to the MetaTrader 5 (MT5) platform and logs in using specified credentials (note: credentials are hardcoded, not from dotenv or os).
- Retrieves and prints the balance and equity of the connected account.
- Retrieves the last 100 one-minute candlesticks for the "EURAUD.a" symbol.
-Converts the time data to a more readable format.
-Prints the price data and the last close price to the console.
-Calculates the mean and standard deviation of the close prices from the retrieved data.
-Determines the upper and lower thresholds for trading.
-Automatically places buy or sell orders based on the calculated thresholds with set TP and SL levels (though the TP and SL levels might need adjustments 
 to avoid "Invalid stops" errors).
-Includes basic error handling for MT5 function calls, such as checking if data retrieval was successful and printing error messages to the console if not.
-Continuously monitors open positions for the "EURAUD.a" symbol and attempts to place new trades if there are no open positions.
Limitations:
- The script does not include logic to manage existing trades beyond the initial TP and SL levels, such as trailing stops or condition-based exits.
- The script is set up to trade only the "EURAUD.a" symbol. It doesn't have the functionality to trade multiple symbols or dynamically select symbols based on certain criteria.
- The error handling in the script is quite basic. More comprehensive error handling and logging would be beneficial to diagnose and handle issues that might occur during runtime.
- The trading strategy implemented in the script is quite simple, based only on the mean and standard deviation of recent close prices. More complex strategies might include multiple indicators, risk management rules, etc.
- Trading parameters such as volume, TP, and SL levels are hardcoded into the script, which doesn't allow for dynamic adjustment based on changing market conditions or account equity.
- The script contains an infinite loop, which means it will run indefinitely until interrupted by the user. This might not be desirable for a production trading system, where more controlled operation and shutdown procedures would be beneficial.
- The script does not include any functionality for backtesting the trading strategy on historical data or optimizing the strategy parameters for better performance.
