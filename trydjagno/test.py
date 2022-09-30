import os
from django.conf import settings
from django.test import TestCase 
from django.contrib.auth.password_validation import validate_password

# Different commands 
# python3 manage.py test (To run all test's).
# self.assertTrue(1==1)
# self.assertEqual(1, 1)
# self.assertNotEqual(1, 2)


class TryDjangoConfigTest(TestCase):
    def test_secret_key_strength(self):
        # print('This is the secret key:', settings.SECRET_KEY)
        # self.assertEqual(settings.SECRET_KEY, 'la2+u2rdceh853y)ddo+7*wpefic%c27%@vu5%l(!hh$#b#)#')
        DATABASE_URL = os.environ.get('DATABASE_URL')
        print('DATABASE_URL', DATABASE_URL)
        try:
            is_strong = validate_password(settings.SECRET_KEY)
        except Exception as e:
            msg = f'Bad Secret_key {e.messages}'
            self.fail(e)

            

        
        