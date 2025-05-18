class Product:
    def _init_(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def get_product_details(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "price": self.price
        }