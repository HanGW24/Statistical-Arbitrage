import pandas as pd
import MetaTrader5 as mt5
import time

# Connect to MT5
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

login = 51171180
password = "w3kYMwKJ"
server = "ICMarkets-Demo"

if not mt5.login(login, password, server):
    print("login() failed, error code =", mt5.last_error())
    quit()

# Retrieve account information
account_info = mt5.account_info()
if account_info is None:
    print("Failed to retrieve account information, error code =", mt5.last_error())
    quit()

print("Account Information:")
print("Balance:", account_info.balance)
print("Equity:", account_info.equity)


# Define the algorithm
def trade_algorithm():
    # Retrieve price data
    symbol = "EURAUD.a"
    price_data = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 100)
    if price_data is None:
        print("Failed to retrieve price data, error code =", mt5.last_error())
        return

    df = pd.DataFrame(price_data)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)

    # Implementing trading logic
    mean_price = df['close'].mean()
    std_price = df['close'].std()
    upper_threshold = mean_price + std_price
    lower_threshold = mean_price - std_price
    current_price = df['close'].iloc[-1]
    print(current_price)

    if current_price > upper_threshold:
        # Opening short position
        place_order(symbol, mt5.ORDER_TYPE_SELL, mt5.symbol_info_tick(symbol).bid)
    elif current_price < lower_threshold:
        # Opening long position
        place_order(symbol, mt5.ORDER_TYPE_BUY, mt5.symbol_info_tick(symbol).ask)


def place_order(symbol, order_type, price):
    point_value = mt5.symbol_info(symbol).point
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.1,
        "type": order_type,
        "price": price,
        "deviation": 20,
        "magic": 123456,
        "comment": "Statistical arbitrage buy" if order_type == mt5.ORDER_TYPE_BUY else "Statistical arbitrage sell",
        "type_filling": mt5.ORDER_FILLING_IOC,
        "tp": price + (10 * point_value) if order_type == mt5.ORDER_TYPE_BUY else price - (10 * point_value),
        "sl": price - (5 * point_value) if order_type == mt5.ORDER_TYPE_BUY else price + (5 * point_value)
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Failed to open trade:", result.comment)
    else:
        print("Trade opened at", price)


# Main function to monitor and trade
def main():
    try:
        while True:
            # Retrieve positions
            positions = mt5.positions_get(symbol="EURAUD.a")
            if positions is not None:
                if len(positions) == 0:
                    trade_algorithm()
                else:
                    # Additional logic for monitoring existing positions can go here
                    time.sleep(1)
            else:
                print("Failed to retrieve positions, error code =", mt5.last_error())
            time.sleep(1)
    except KeyboardInterrupt:
        print("Execution stopped by user.")
    finally:
        mt5.shutdown()


if __name__ == "__main__":
    main()
