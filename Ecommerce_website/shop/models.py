from django.db import models
from django.core.validators import EmailValidator, MaxLengthValidator
# Create your models here.
CATEGORY_CHOICES = (
    ('Electronics', 'Electronics'),
    ('Home and Decor', 'Home & Decor'),
    ("Men's Fashion", "Men's Fashion"),
    ("Women's Fashion", "Women's Fashion"),
    ("Furniture", "Furniture"),
)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=350)
    pub_date = models.DateField()
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default="Electronics")
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    subcategory = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="", validators=[EmailValidator()])
    phone = models.CharField(max_length=70, default="", validators=[MaxLengthValidator(13)])
    desc = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name


class Orders(models.Model):
    items_json = models.CharField(max_length=5000)
    f_name = models.CharField(max_length=99, default="")
    l_name = models.CharField(max_length=99, default="")
    address = models.CharField(max_length=1500, default="")
    amount = models.FloatField(default=0)
    email = models.CharField(max_length=75, default="", validators=[EmailValidator()])
    phone = models.CharField(max_length=70, default="", validators=[MaxLengthValidator(13)])
    country = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    pincode = models.CharField(max_length=10, default="")


class OrderUpdate(models.Model):
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    email = models.CharField(max_length=75, default="", validators=[EmailValidator()])
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
