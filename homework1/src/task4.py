# function that calculates the final price of a product after 
#applying a given discount percentage inside of a function

def calculate_discount(price, discount):
    if discount < 0 or discount >100:
        #print("Discount percentage must be between 0 and 100")
        return price
   
   #how to calculate the discounted amount
    discounted_amount = price * (discount/100)
    #final price of that product calculation
    final_price = price - discounted_amount

#return final price
    return final_price
