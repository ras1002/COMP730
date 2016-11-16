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

    def test_can_process(self):
        '''
        Verify that can_process() returns True if fund balance > transaction amount
        Which ensures that there is enough money in the fund to cover the transaction
        '''
        u = User.objects.get(username="test_user")
        f = Fund.objects.get(owner=u)
        t = Transaction(amount=10, category="test", fund=f)
        self.assertGreater(t.amount, f.balance)
        self.assertFalse(t.can_process())
        f.balance = 100
        self.assertLess(t.amount, f.balance)
        self.assertTrue(t.can_process())

    def test_process(self):
        '''
        Verify transaction process() method deducts money from fund
        '''
        u = User.objects.get(username="test_user")
        f = Fund.objects.get(owner=u)
        t = Transaction(amount=5, category="test_trans", fund=f)
        self.assertGreater(t.amount, f.balance)
        self.assertFalse(t.process())
        f.balance = 10
        f.save()
        self.assertEqual(f.balance, 10)
        self.assertEqual(t.amount, 5)
        t.process()
        self.assertEqual(f.balance, 5)        













