purchase_price = float(input("Enter purchase price per share: "))
current_price = float(input("Enter current stock price: "))
quantity = float(input("Enter quantity of shares: "))

value_change = (current_price - purchase_price) * quantity

print(f"Stock value change: ${value_change:.2f}")