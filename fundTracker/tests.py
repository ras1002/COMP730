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
        ''''
        Verifies negative deposits return false without affecting fund balance
        Positive deposits increment balance as expected
        '''
        u = User.objects.get(username="test_user")
        f = Fund.objects.get(owner=u)
        x = f.balance
        self.assertFalse(f.deposit(-10))
        self.assertEqual(x, f.balance)
        self.assertTrue(f.deposit(10))
        self.assertLess(x, f.balance)

class TransactionMethodTests(TestCase):

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

    def test_process_method(self):
        u = User.objects.get(username="test_user")
        f = Fund.objects.get(owner=u)
        t = Transaction(amount=5, category="test_trans", fund=f)
        f.balance = 10
        f.save()
        self.assertEqual(f.balance, 10)
        
        













