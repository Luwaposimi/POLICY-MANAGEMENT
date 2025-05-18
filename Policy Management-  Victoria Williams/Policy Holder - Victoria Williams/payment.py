class Payment:
    def _init_(self, payment_id, policyholder_id, product_id, amount):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount

    def get_payment_details(self):
        return {
            "payment_id": self.payment_id,
            "policyholder_id": self.policyholder_id,
            "product_id": self.product_id,
            "amount": self.amount
        }