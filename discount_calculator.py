** start of main.py **

def apply_discount(price , discount):
    if not isinstance(price, (int, float)):
        return('The price should be a number')
    elif not isinstance(discount , (int,float)):
        return('The discount should be a number')
    elif price <= 0:
        return('The price should be greater than 0')
    elif discount < 0 or discount > 100 :
        return('The discount should be between 0 and 100')
    else:
        dicount_applied = (discount/100) * price
        final_price = price - dicount_applied
        return(final_price)
        



      

** end of main.py **

