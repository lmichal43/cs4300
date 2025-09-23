def calculate_discount(price, discount):
    if discount < 0 or discount >100:
        #print("Discount percentage must be between 0 and 100")
        return price
    discounted_amount = price * (discount/100)
    final_price = price - discounted_amount

    return final_price
