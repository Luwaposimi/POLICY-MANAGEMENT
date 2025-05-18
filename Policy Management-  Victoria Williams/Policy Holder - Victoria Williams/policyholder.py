class PolicyHolder:
    def _init_(self, policyholder_id, name, email):
        self.policyholder_id = policyholder_id
        self.name = name
        self.email = email
        self.payments = []
        self.products = []

    def add_payment(self, payment):
        self.payments.append(payment)

    def add_product(self, product):
        self.products.append(product)

    def get_account_details(self):
        return {
            "policyholder_id": self.policyholder_id,
            "name": self.name,
            "email": self.email,
            "products": [product.product_name for product in self.products],
            "total_payments": sum(payment.amount for payment in self.payments)
        }