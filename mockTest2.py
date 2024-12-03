import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from app import create_app
from services.productService import save
from models.models import Product

class TestSaveProduct(unittest.TestCase):
    @patch('services.productService.Session')
    def test_save_product(self, mock_session):
        # Set up application context
        app = create_app('DevelopmentConfig')  # Use your testing configuration
        with app.app_context():
            faker = Faker()

            # Create mock product data
            mock_product_data = {
                'name': faker.name(),
                'price': faker.pyfloat(left_digits=3, right_digits=2, positive=True)
            }

            # Mock Product instance
            mock_product = Product(name=mock_product_data['name'], price=mock_product_data['price'])
            mock_product.id = 1  # Simulate ID assignment after commit

            # Mock session behavior
            mock_session_instance = mock_session.return_value.__enter__.return_value
            mock_session_instance.refresh = MagicMock()

            # Call the function
            result = save(mock_product_data)

            # Verify interactions
            mock_session_instance.add.assert_called_once()
            mock_session_instance.commit.assert_called_once()
            mock_session_instance.refresh.assert_called_once()

            # Assert the result
            self.assertEqual(result.name, mock_product_data['name'])
            self.assertEqual(result.price, mock_product_data['price'])
            #self.assertEqual(result.id, 1)



'''
class FindProduct(unittest.TestCase):
    @patch('db.session.execute')
    def test_find_products(self):
        app = create_app('DevelopmentConfig')  # Use your testing configuration
        with app.app_context():
            response = app.get('/products')
            results = response.get_json()
            self.assertEqual(results['status'], 'success')
            '''


if __name__ == '__main__':
    unittest.main()