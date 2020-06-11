from django.db import models
from django.utils import timezone
import requests
import environ
import base64
from .category import Category

env = environ.Env()


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    code = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    age_limit = models.IntegerField(default=None)
    age_verification = models.TextField(null=True)
    amount = models.IntegerField(null=True)
    avail_since = models.IntegerField(null=True)
    average_rating = models.CharField(null=True, max_length=50)
    base_price = models.DecimalField(
        decimal_places=6, max_digits=15, null=True)
    buy_now_url = models.CharField(default=None, max_length=50)
    #
    # category_ids = models.ManyToManyField(Category)
    company_id = models.IntegerField(default=None)
    details_layout = models.CharField(default=None, max_length=50)
    discount = models.CharField(default=None, null=True, max_length=50)
    discount_prc = models.CharField(default=None, null=True, max_length=50)
    # discounts = models.TextField()
    discussion_thread_id = models.CharField(default=None, max_length=50)
    discussion_type = models.CharField(default=None, max_length=50)
    edp_shipping = models.CharField(default=None, max_length=50)
    exceptions_type = models.CharField(default=None, max_length=50)
    facebook_obj_type = models.CharField(default=None, max_length=50)
    free_shipping = models.CharField(default=None, max_length=50)
    has_options = models.CharField(default=None, max_length=50)
    height = models.CharField(default=None, max_length=50)
    # image_pairs = models.TextField(default=None)
    is_edp = models.CharField(default=None, max_length=50)
    is_op = models.CharField(default=None, max_length=50)
    is_oper = models.CharField(default=None, max_length=50)
    is_pbp = models.CharField(default=None, max_length=50)
    is_returnable = models.CharField(default=None, max_length=50)
    length = models.CharField(default=None, max_length=50)
    list_price = models.DecimalField(
        decimal_places=6, max_digits=15, default=None)
    list_qty_count = models.CharField(default=None, max_length=50)
    localization = models.CharField(default=None, max_length=50)
    low_avail_limit = models.CharField(default=None, max_length=50)
    main_category = models.CharField(default=None, max_length=50)
    # 'main_pair', '
    max_qty = models.CharField(default=None, max_length=50)
    min_qty = models.CharField(default=None, max_length=50)
    options_type = models.CharField(default=None, max_length=50)
    out_of_stock_actions = models.CharField(default=None, max_length=50)
    price = models.CharField(default=None, max_length=50)
    product = models.CharField(default=None, max_length=50)
    product_code = models.CharField(default=None, max_length=50)
    # product_features',
    # product_id = models.CharField(default=None)
    product_options = models.CharField(default=None, max_length=50)
    list_discount = models.IntegerField(null=True)
    list_discount_prc = models.CharField(null=True, max_length=50)
    # promotions',
    # qty_content = models.TextField()
    qty_step = models.CharField(default=None, max_length=50)
    return_period = models.CharField(default=None, max_length=50)
    selected_options = models.CharField(default=None, max_length=50)
    seo_name = models.CharField(default=None, max_length=50)
    seo_path = models.CharField(default=None, max_length=50)
    shipping_freight = models.CharField(default=None, max_length=50)
    shipping_params = models.CharField(default=None, max_length=50)
    # 'stickers',
    tax_ids = models.CharField(default=None, max_length=50)
    taxed_list_price = models.CharField(null=True, max_length=50)
    taxed_original_price = models.CharField(null=True, max_length=50)
    timestamp = models.CharField(default=None, max_length=50)
    tracking = models.CharField(default=None, max_length=50)
    unlimited_download = models.CharField(default=None, max_length=50)
    usergroup_ids = models.CharField(default=None, max_length=50)
    weight = models.CharField(default=None, max_length=50)
    width = models.CharField(default=None, max_length=50)
    zero_price_action = models.CharField(default=None, max_length=50)
    updated_timestamp = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    ITEMS_PER_PAGE = 600

    @classmethod
    def sync_product(cls):
        total_items = int(cls.get_total_items())
        total_pages = total_items // cls.ITEMS_PER_PAGE + 1
        print(f"{total_items}, {total_pages}")
        for p in range(37, total_pages):
            print(f"{p}目")
            products = cls.get_products(page=p)
            # def filter_product(f, d):
            # return {k:v for k,v in d.items() if f(k,v)}
            for item in products:
                # import pdb; pdb.set_trace()
                r = cls.filter_product(product=item)
                print(r)
                product = cls(**r)
                product.save()

    @classmethod
    def get_response(cls, items_per_page=ITEMS_PER_PAGE, page=1):
        session = requests.Session()
        session.headers.update(cls.request_header())
        r = session.get('%s/%s' % (cls.api_url(), '/products'), params={
                        'items_per_page': items_per_page, 'page': page})
        return r

    @classmethod
    def api_url(cls):
        return env('CSCART_API_URL')

    @classmethod
    def request_header(cls):
        src = '%s:%s' % (env('EMAIL'), env('SECRET_KEY'))
        token = 'Basic %s' % base64.b64encode(
            src.encode('utf-8')).decode('ascii')
        return {'Authorization': token}

    @classmethod
    def get_total_items(cls) -> int:
        return cls.get_response(items_per_page=1).json()['params']['total_items']

    @classmethod
    def get_products(cls, items_per_page=ITEMS_PER_PAGE, page=1):
        return cls.get_response(items_per_page, page).json()['products']

    @classmethod
    def filter_product(cls, product):
        return dict([(k, v) for k, v in product.items() if k not in
                     ['category_ids',
                      'stickers', 'main_pair', 'product_features', 'discounts', 'qty_content',
                      'image_pairs', 'promotions']])
