
def calculate_discount(price,discount_percent):

    if discount_percent>=20:
        discount=(discount_percent)/100*price
        return price-discount
    else:
        return price

# Prompt the user for input
try:
    price=float(input("Enter the original price of the item: "))
    discount_percent=float(input("Enter the dicount percentage:"))

    #Calculate the final price
    final_price=calculate_discount(price,discount_percent)

    #Output the result
    if discount_percent>=20:
        print(f"After applying a {discount_percent}% discount, the final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${price:.2f}")   
except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")