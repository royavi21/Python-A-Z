prices = [100, 200, 300]

discount = 10

final_prices = []

for p in prices:
    final_price = p - (p * discount / 100)
    final_prices.append(final_price)
    
print(final_prices)

# for loop use more time and memory compared to list comprehension 