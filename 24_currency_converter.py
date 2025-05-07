import requests
def main():
 print("currency_converter")
 print("Getting exchange rates...")
 try:
  response=requests.get("https://open.er-api.com/v6/latest/USD")
  rates=response.json()['rates']
  print("👉 got rates successfully")

 except:
  print("❌ Error:could not connect to exchange rate API")
 print("popular:USD EUR GBP JPY CAD AUD CNY PKR")
 while True:
  print(" Enter details")
  from_currency=input("from curency code(e.g USD:)").upper()
  if from_currency not in rates:
   print(f"❌ invalid code:{from_currency}")
   continue
  to_currency=input("to currency code(e.g EUR)").upper()
  if to_currency not in rates:
   print(f"❌ invalid code:{to_currency}")
   continue
  try:
   amount=float(input(f"amount in {from_currency}:"))
  except:
   print("❌enter a valid number")
   continue
  amount_in_usd=amount/rates[from_currency]
  result=amount_in_usd*rates[to_currency]
  print(f" result: {amount} {from_currency}= {result:.2f} {to_currency}")
  print(f" rates 1:{rates[to_currency]/rates[from_currency]:.4f} {to_currency}")
  if not input(" convert again? (y/n):").lower().startswith("y"):
   print("🌝thanks for playing")
   break 
main()