import csv
from policyholder import PolicyHolder
from product import Product
from payment import Payment

ph1 = PolicyHolder(1, "Akinde Michael", "oluwaferanmiakinde01@gmail.com")
ph2 = PolicyHolder(2, "Victoria Williams", "luwaposimi@gmail.com")

product1 = Product(101, "Health Insurance", 500)
product2 = Product(102, "Car Insurance", 300)

ph1.add_product(product1)
ph1.add_product(product2)
ph2.add_product(product1)

payment1 = Payment(1002, 1, 101, 500)
payment2 = Payment(1003, 1, 102, 300)
payment3 = Payment(1004, 2, 101, 600)

ph1.add_payment(payment1)
ph1.add_payment(payment2)
ph2.add_payment(payment3)

policyholders = [ph1, ph2]
for ph in policyholders:
    if ph.payments:
        print("Account Details:")
        print(ph.get_account_details())

with open('account_details.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["policyholder_id", "name", "email", "products", "total_payments"])
    writer.writeheader()
    for ph in policyholders:
        if ph.payments:
            writer.writerow(ph.get_account_details())