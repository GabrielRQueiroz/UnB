# Parcelas: Desconto
disc_table = {
    1: 0.95,
    2: 1,
    3: 1.05,
    4: 1.1,
}

def f_price(price, times):
    final_price = price * disc_table[times]
    price_per_time = final_price/times
    return f"{final_price:.2f} {price_per_time:.2f}"
    
print(f_price(150, 4))
print(f_price(200, 3))
print(f_price(45, 1))
print(f_price(70.25, 2))