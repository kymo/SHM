#encoding:utf-8
import hashlib
from models import Account
class CustionBackend:
    def authenticate(self, email = None, password = None):
        print email, password
        try:
            user = Account.objects.get(email = email)
        except Account.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                print 'yes'
                return user
        return None
    
    def get_user(self, user_id):
        try:
            return Account.objects.get(pk = user_id)
        except Account.DoesNotExist:
            return None
