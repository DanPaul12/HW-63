import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services.productService import save

class TestSaveProduct(unittest.TestCase):
    @patch('services.productService.Session')
    def test_save_product(self):
        
        faker = Faker()
        mock_product = MagicMock()
        mock_product.name = faker.name()
        mock_product.price = faker.float()