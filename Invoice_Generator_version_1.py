#Invoice Generator

def calculate_total_price(units, unit_price):  
    total_price = units * unit_price
    return total_price

def get_and_check_numeric(units, unit_price= False):
    while True:
        try:
            value= float(input(units)) if unit_price else int(input(units))
            if value <= 0:
             print("The amount entered is not correct, it has to be more than 0 ")
             print("")
            else:
                return value
        except ValueError:
            print("Input not valid, please enter a number")
            print("")


def main():
    print("")
    print("Welcome to your store!")
    print("")
    product_name = input("Insert the product name: ")
    units = get_and_check_numeric("Insert the quantity purchases: ")
    unit_price = get_and_check_numeric ("Insert the unit price of the product: ", unit_price=True)
    print("")
    


    total_price = calculate_total_price(units, unit_price)
    iva = total_price * 0.21
    total_price_with_iva = total_price + iva

    print("")
    print("Purchased Receipt: ")
    print(f"Product: {product_name}")
    print(f"units: {units}")
    print(f"Unit price: {unit_price:.2f}€")
    print(f"Total: {total_price:.2f}€")
    print(f"Iva (21%): {iva:.2f}€")
    print(f"Total with iva: {total_price_with_iva:.2f}€")
    print("")
   

main()