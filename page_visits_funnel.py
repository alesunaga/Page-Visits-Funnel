import codecademylib3
import pandas as pd

# Load datasets for each stage in the customer journey, parsing the date columns for each file.
visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

# 1. Display the first five rows of each dataset to understand their structure.
# print(visits.head(5))
# print(cart.head(5))
# print(checkout.head(5))
# print(purchase.head(5))

# 2. Merge 'visits' and 'cart' datasets to see which visitors placed items in the cart.
visits_cart = pd.merge(visits, cart, how='left')

# 3. Calculate the number of rows and columns in the merged DataFrame 'visits_cart'.
rows_visit, columns = visits_cart.shape
# print("Number of rows:", rows_visit)
# print("Number of columns:", columns)

# 4. Filter to see visitors who did not add items to their cart by checking where 'cart_time' is null.
# print(visits_cart[visits_cart.cart_time.isnull()])
rows_cart, columns = visits_cart[visits_cart.cart_time.isnull()].shape
# print(rows_cart)

# 5. Calculate the percentage of visitors who only visited without adding items to their cart.
# print('The percentage only visited is ' + str((rows_visit - rows_cart) / rows_visit))

# 6. Calculate the percentage of visitors who added items to their cart but did not proceed to checkout.
rows_purchase, columns = purchase.shape
# print("Number of rows:", rows_purchase)
# print('The percentage that placed a t-shirt in their cart but did not checkout is ' + str((rows_cart - rows_purchase) / rows_cart))

# 7. Merge 'visits_cart' and 'checkout', and then merge this result with 'purchase' to get the full journey.
visits_cart_checkout = pd.merge(visits_cart, checkout)
all_data = pd.merge(visits_cart_checkout, purchase)
print(all_data.head())

# 8. Calculate the percentage of users who reached checkout but did not complete a purchase.
rows_checkout, columns = checkout.shape
rows_purchase, columns = purchase.shape
# print('The percentage of clients that got to checkout but did not purchase is ' + str((rows_checkout - rows_purchase) / rows_checkout))

# 9. Summary print statements for all three funnel stages: visits without cart, cart without checkout, and checkout without purchase.
print('The percentage only visited is ' + str((rows_visit - rows_cart) / rows_visit))
print('The percentage that placed a t-shirt in their cart but did not checkout is ' + str((rows_cart - rows_purchase) / rows_cart))
print('The percentage of clients that got to checkout but did not purchase is ' + str((rows_checkout - rows_purchase) / rows_checkout))

# 10. Calculate the time taken from the visit to purchase and create a new column 'average_time' to store this duration.
all_data['average_time'] = all_data.purchase_time - all_data.visit_time

# 11. Print the 'average_time' column to examine the purchase duration for each customer.
print(all_data.average_time)

# 12. Calculate and print the average time to complete a purchase for all customers.
print('The average time to purchase is ' + str(all_data.average_time.mean()))
