from django.test import TestCase
from django.contrib.auth.models import User
from .models import Fund, Transaction


# Create your tests here.

class FundMethodTests(TestCase):

    def setUp(self):
        User.objects.create_user("test_user", password="bar")
        u = User.objects.get(username="test_user")
        f = Fund(
            owner = u,
        )
        f.save()
        t = Transaction(
            amount=10,
            category='test transaction',
            fund=f,
        )

    def test_deposit(self):
        u = User.objects.get(username="test_user")
        f = Fund.objects.get(owner=u)
        x = f.balance
        print(x)
        self.assertFalse(f.deposit(-10))
        self.assertEqual(x, f.balance)
        self.assertTrue(f.deposit(10))
        self.assertLess(x, f.balance)
        print(f.balance)
