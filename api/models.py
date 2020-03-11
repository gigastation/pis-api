from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)


class Product(models.Model):
    product_id = models.IntegerField()
    name = models.TextField()
    code = models.TextField()
    product_type = models.TextField()
    status = models.TextField()
    age_limit = models.IntegerField(default=None)
    age_verification = models.TextField(null=True)
    amount = models.IntegerField(null=True)
    avail_since = models.IntegerField(null=True)
    average_rating = models.IntegerField(null=True)
    base_price = models.DecimalField(
        decimal_places=6, max_digits=15, null=True)
    buy_now_url = models.TextField(default=None)
    #
    category_ids = models.ManyToManyField(Category)
    company_id = models.IntegerField(default=None)
    details_layout = models.TextField(default=None)
    discount = models.TextField(default=None)
    discount_prc = models.TextField(default=None)
    # discounts = models.TextField()
    discussion_thread_id = models.TextField(default=None)
    discussion_type = models.TextField(default=None)
    edp_shipping = models.TextField(default=None)
    exceptions_type = models.TextField(default=None)
    facebook_obj_type = models.TextField(default=None)
    free_shipping = models.TextField(default=None)
    has_options = models.TextField(default=None)
    height = models.TextField(default=None)
    image_pairs = models.TextField(default=None)
    is_edp = models.TextField(default=None)
    is_op = models.TextField(default=None)
    is_oper = models.TextField(default=None)
    is_pbp = models.TextField(default=None)
    is_returnable = models.TextField(default=None)
    length = models.TextField(default=None)
    list_price = models.DecimalField(
        decimal_places=6, max_digits=15, default=None)
    list_qty_count = models.TextField(default=None)
    localization = models.TextField(default=None)
    low_avail_limit = models.TextField(default=None)
    main_category = models.TextField(default=None)
    # 'main_pair', '
    max_qty = models.TextField(default=None)
    min_qty = models.TextField(default=None)
    options_type = models.TextField(default=None)
    out_of_stock_actions = models.TextField(default=None)
    price = models.TextField(default=None)
    product = models.TextField(default=None)
    product_code = models.TextField(default=None)
    # product_features',
    product_id = models.TextField(default=None)
    product_options = models.TextField(default=None)
    # promotions',
    #qty_content = models.TextField()
    qty_step = models.TextField(default=None)
    return_period = models.TextField(default=None)
    selected_options = models.TextField(default=None)
    seo_name = models.TextField(default=None)
    seo_path = models.TextField(default=None)
    shipping_freight = models.TextField(default=None)
    shipping_params = models.TextField(default=None)
    # 'stickers',
    tax_ids = models.TextField(default=None)
    taxed_list_price = models.TextField(default=None)
    taxed_original_price = models.TextField(default=None)
    timestamp = models.TextField(default=None)
    tracking = models.TextField(default=None)
    unlimited_download = models.TextField(default=None)
    usergroup_ids = models.TextField(default=None)
    weight = models.TextField(default=None)
    width = models.TextField(default=None)
    zero_price_action = models.TextField(default=None)
    updated_timestamp = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
