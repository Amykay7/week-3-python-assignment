# Define the calculate_discount function
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price


# enter the original price of the item
price = float(input("1000: "))

# enter the discount percentage
discount_percent = float(input("20: "))

# Call the calculate_discount function and store the result
final_price = calculate_discount(price, discount_percent)

# Print the final price after applying the discount, or the original price if no discount was applied
print(f"The final price is: {final_price}")


