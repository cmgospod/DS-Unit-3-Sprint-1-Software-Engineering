import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Ensures the default weight is 20"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealyboom(self):
        """Tests stealability and explode"""
        prod = Product(name='Test Product', price=100,
                       weight=100, flammability=100)
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    """Making sure the report functions properly."""
    def test_default_num_products(self):
        """Test default products being 30"""
        case = generate_products()
        self.assertEqual(len(case), 30)

    def test_legal_names(self):
        """Tests that the names have proper Acme names"""
        case = generate_products()
        for product in case:
            adjective, noun = product.name.split()
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()
