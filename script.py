hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Prices and Cuts
total_price = 0

for price in prices:
  total_price += price

average_price = total_price/len(prices)

print("Average Haircut Price:", average_price)

new_prices = [price-5 for price in prices]

print(new_prices)

#Revenue
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])

print("Total Revenue: {}".format(total_revenue))

average_daily_revenue = total_revenue/7
print(average_daily_revenue)

cuts_under_30 = [(new_prices[i]) for i in range(len(new_prices)) if new_prices[i]<30]    


print(cuts_under_30)