from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class Product(Model):
    class Meta:
        table_name = 'products'
        region = 'ap-northeast-1'
        write_capacity_units = 1
        read_capacity_units = 1
        host = 'http://dynamodb:8000'
        aws_access_key_id = 'my_access_key_id'
        aws_secret_access_key = 'my_secret_access_key'
    product_id = UnicodeAttribute(hash_key=True)
