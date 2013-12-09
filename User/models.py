from django.db.models import *
import hashlib
from utils.hashs import create_nid
# Create your models here.
class Account(Model):
    nick_name = CharField(max_length = 128, null = False)
    real_name = CharField(max_length = 128, null = False)
    school_num = CharField(max_length = 32, null = True)
    password = CharField(max_length = 64, null = False)
    email = EmailField()
    qq = CharField(max_length = 12, null = False)
    phone = CharField(max_length = 16, null = False)
    last_login = DateTimeField(null = True)
    nid = CharField(max_length = 64, null = True)
    # user_pri
    # 0: normal user
    # 1: super user
    user_pri = CharField(max_length = 4, default = 0)
    person_intro = TextField(null = False)
    
    def is_authenticated(self):
        return True
    
    def hashed_password(self, password = None):
        if not password:
            return self.password
        else:
            return hashlib.md5(password).hexdigest()
    
    def check_password(self, password):
        if self.hashed_password(password) == self.password:
            return True
        return False
    
    @classmethod
    def create_user(self, user_params):
        """
        create a user and save into db
        """
        try:
            user = Account(nick_name = user_params['nickname'],
                real_name = user_params['realname'],
                password = hashlib.md5(user_params['password']).hexdigest(),
                email = user_params['email'],
                qq = user_params['qq'],
                person_intro = user_params['intro'],
                phone = user_params['phone'])
            user.save()
            nid = create_nid(user.id)
            user.nid = nid
            user.save()
            return user
        except Exception,e:
            print e
            return None
                
    @classmethod
    def by_nid(cls, nid):
        try:
            user = cls.objects.get(nid = nid)
        except:
            return None
        return user
    
    class Meta:
        ordering = ['-id']
        db_table = 'account'
    
