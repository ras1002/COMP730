from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from .models import Goal

import decimal

# Create your tests here

class GoalMethodTests(TestCase):

    def setUp(self):
        User.objects.create_user("test_user", password="bar")
        u = User.objects.get(username="test_user")
        Goal.objects.create(
            title = 'test goal',
            goal_amount = 999.99,
            current_saved = 0,
            description = 'test case for Goal class',
            owner = u,
        )

    @unittest.expectedFailure
    def test_was_goal_amount_exceeded(self):
        '''
        Verifies Goal objects can not be created with goal_amounts
        exceeding 9999.99
        '''
        g = Goal.objects.get(title='test goal')
        g.goal_amount = 10000.00
        g.save()

    def test_was_goal_created(self):
        '''
        Tests to ensure that Goal objects can be created
        '''
        g = Goal.objects.get(title='test goal')
        self.assertIsInstance(g, Goal)

    def test_goal_variable_types(self):
        '''
        Tests that all goal class attributes are
        of the appropriate data type
        '''
        g = Goal.objects.get(title='test goal')
        self.assertIsInstance(g.title, str)
        self.assertIsInstance(g.goal_amount, decimal.Decimal)
        self.assertIsInstance(g.current_saved, decimal.Decimal)
        self.assertIsInstance(g.description, str)
        self.assertIsInstance(g.owner, User)

    def test_is_goal_completed(self):
        '''
        Goals that are completed return correct values for
        the is_completed() method
        '''
        g = Goal.objects.get(title='test goal')
        self.assertEqual(0, g.current_saved)
        g.current_saved = 10
        self.assertEqual(10, g.current_saved)
        self.assertFalse(g.is_completed())
        g.current_saved = g.goal_amount + 1
        self.assertTrue(g.is_completed())

    def test_add_savings(self):
        '''
        add_savings() should return false if a negative x is passed
        in, otherwise it should increment the current_saved by x
        '''
        g = Goal.objects.get(title='test goal')
        x = g.current_saved #base case for current_saved
        self.assertFalse(g.add_savings(-10))
        #ensure current_saved was not changed when passing a negative value
        self.assertEqual(x, g.current_saved)
        self.assertTrue(g.add_savings(10))
        #ensure current_saved was changed when passing a positive value
        self.assertLess(x, g.current_saved)
