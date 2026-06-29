class Bill:

    TAX = 0.18

    def calculate_bill(self, products):

        subtotal = sum(product.total_price() for product in products)
        tax = subtotal * self.TAX
        total = subtotal + tax

        return subtotal, tax, total