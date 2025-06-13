print("track live stock using python")
import yfinance as yf

symbol=input("Enter the Symbol to track: ").upper()
stock=yf.Ticker(symbol)
try:
    price=stock.history(period="1d")["Close"].iloc[-1]
    print(f"The Current price of {symbol} is :${price:2f}")
    
except IndexError:
    print("can not find stock with this symbol")

