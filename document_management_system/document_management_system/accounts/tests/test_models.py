from django.test import TestCase
from accounts.models import Account

class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(name="username")
        Account.objects.create(name=" email")

    def test_Accounts(self):
        
        username = Account.objects.get(name="username")
        email = Account.objects.get(name=" email")
        
        self.assertEqual(username.insert(), 'username')
        self.assertEqual(email.insert(), 'email')