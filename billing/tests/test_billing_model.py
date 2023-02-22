from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Invoice, ItemLine
import datetime


User = get_user_model()

class TestBillingCreate(TestCase):
    """Test billing models creation"""

    def setUp(self):
        self.email = "mymail@mail.com"
        self.username = "myusername"
        self.password = "MytestPass"
        self.description = "Simple itemline description"
        self.quantity = 5
        self.price = 50
        self.taxed = True
        self.date = datetime.datetime.today()
        self.user = User.objects.create_user(
            email = self.email,
            username = self.username,
            password = self.password
		)
        self.invoice = Invoice.objects.create(
			user = self.user,
			date = self.date,
			due_date = self.date + datetime.timedelta(days = 5)
		)

    def test_create_invoice(self):
        """Test invoice created successfully"""
        
        self.assertEqual(self.invoice.date, self.date)
        self.assertEqual(self.invoice.user, self.user)
  
    def test_create_itemline(self):
        """Test itemline is created successfully"""
        
        self.itemline = ItemLine.objects.create(
             invoice = self.invoice,
             quantity = 5,
             description = self.description,
             price = self.price,
             taxed = self.taxed
		)
        
        self.assertEqual(self.itemline.invoice, self.invoice)
        self.assertEqual(self.itemline.invoice.user, self.user)
        