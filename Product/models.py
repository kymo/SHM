from django.db.models import *
import hashlib
from utils.hashs import create_nid
from User.models import Account

class Comment(Model):
    content = CharField(max_length = 256, null = False)
    class Meta:
        ordering = ['-id']
        db_table = 'comment'

# Create your models here.
class ProductToSell(Model):
    owner = ForeignKey( Account, related_name = 'person_product_to_sell)')
    product_name = CharField(max_length = 128, null = False)
    #broad_type = CharField(max_length = 128, null = False)
    #sub_type = CharField(max_length = 32, null = True)
    #belong_campus = CharField(max_length = 128, null = False)
    #trade_type = CharField(max_length = 32, null = False)
    #purity = CharField(max_length = 32, null = False)
    big_img = ImageField(upload_to = 'big_img', height_field = 1024, width_field = 1024, null = False)
    small_img = ImageField(upload_to = 'small_img', height_field = 512, width_field = 512, null = False)
    #price = CharField(max_length = 32, null = False)
    #trade_title = CharField(max_length = 64, null = False)
    #trade_detail = CharField(max_length = 256, null = False)
    #release_time = DateTimeField(null = True)
    #trade_status = CharField(max_length = 32, null = False)
    #comment = ForeignKey( Comment, related_name = 'comment_product_to_sell')
    nid = CharField(max_length = 64, null = True)
    
    @classmethod
    def create_product_to_sell(self, product_params):
        """
        create a product and save into db
        """
        try:
            product_to_sell = ProductToSell( owner = product_params['owner'],
                    product_name = product_params['productname'],
                    #broad_type = product_params['broadtype'],
                    #sub_type = product_params['subtype'],
                    #belong_campus = product_params['belongcampus'],
                    #trade_type = product_params['tradetype'],
                    #purity = product_params['purity'],
                    big_img = product_params['image'],
                    small_img = product_params['image'],
                    #price = product_params['price'],
                    #trade_title = product_params['tradetitle'],
                    #trade_detail = product_params['tradedetail'],
                    #release_time = product_params['releasetime'],
                    #trade_status = product_params['tradestatus'],
                    #comment = product_params['comment'])
                    )
            product_to_sell.save()
            nid = create_nid(product.id)
            product.nid = nid
            product.save()
            return product
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
        db_table = 'product_to_sell'
        
class ProductToBuy(Model):
    owner = ForeignKey( Account, related_name = 'person_product_to_buy')
    product_name = CharField(max_length = 128, null = False)
    broad_type = CharField(max_length = 128, null = False)
    sub_type = CharField(max_length = 32, null = True)
    belong_campus = CharField(max_length = 128, null = False)
    trade_type = CharField(max_length = 32, null = False)
    purity = CharField(max_length = 32, null = False)
    big_img = ImageField(upload_to = 'big_img', height_field = 1024, width_field = 1024, null = False)
    small_img = ImageField(upload_to = 'small_img', height_field = 512, width_field = 512, null = False)
    price = CharField(max_length = 32, null = False)
    trade_title = CharField(max_length = 64, null = False)
    trade_detail = CharField(max_length = 256, null = False)
    release_time = DateTimeField(null = True)
    trade_status = CharField(max_length = 32, null = False)
    comment = ForeignKey( Comment, related_name = 'comment_product')
    nid = CharField(max_length = 64, null = True)
    
    @classmethod
    def create_product_to_buy(self, product_params):
        """
        create a product and save into db
        """
        try:
            product_to_sell = ProductToSell( owner = product_params['owner'],
                    broad_type = product_params['broadtype'],
                    sub_type = product_params['subtype'],
                    belong_campus = product_params['belongcampus'],
                    trade_type = product_params['tradetype'],
                    purity = product_params['purity'],
                    #big_img = product_params['bigimg'],
                    #small_img = product_params['smallimg'],
                    price = product_params['price'],
                    trade_title = product_params['tradetitle'],
                    trade_detail = product_params['tradedetail'],
                    release_time = product_params['releasetime'],
                    trade_status = product_params['tradestatus'],
                    comment = product_params['comment'])
            product_to_sell.save()
            nid = create_nid(user.id)
            user.nid = nid
            user.save()
            return product
        except Exception,e:
            print e
            return None

    @classmethod
    def delete_product_to_buy(cls, nid):
        try:
            product = cls.objects.get(nid = nid)
        except:
            return None
        
    @classmethod
    def by_nid(cls, nid):
        try:
            product = cls.objects.get(nid = nid)
        except:
            return None
        return product

    @classmethod
    def add_comment(cls, nid, comment):
        try:
            product = cls.objects.get(nid = nid)
        except:
            return None
        product.comment.add(comment)

    class Meta:
        ordering = ['-id']
        db_table = 'product_to_buy'
