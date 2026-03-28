ticker = input("Enter stock ticker symbol: ")
shares = float(input("Enter number of shares: "))
price = float(input("Enter cost per share: "))

investment = shares * price

print(f"{ticker} investment amount: ${investment:.2f}")