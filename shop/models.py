from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    pub_date = models.DateField
    category = models.CharField(max_length=50,default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images',default='')

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField( primary_key=True)
    name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='')
    phone = models.CharField(max_length=50,default='')
    desc = models.CharField(max_length=500,default='')

    def __str__(self):
        return str(self.msg_id)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_JSON = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)

