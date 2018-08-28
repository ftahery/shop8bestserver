# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

category_choices = (
    ('ring', 'RING'),
    ('bracelet', 'BRACELET'),
    ('necklace', 'NECKLACE'),
    ('chain', 'CHAIN'),
    ('earring', 'EARRING'),
    ('anklet', 'ANKLET')
)


class Items(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_color = models.CharField(max_length=20)
    item_type = models.CharField(max_length=10, choices=category_choices, default='bracelet')
    item_carat = models.IntegerField()
    item_price = models.DecimalField(max_digits=5, decimal_places=3)
    item_weight = models.DecimalField(max_digits=10, decimal_places=3)
    item_quantity = models.IntegerField()
    item_image = models.ImageField(upload_to='images')

    def __str__(self):
        return "{}".format(str(self.item_id) + " " + str(self.item_name))


class ItemImages(models.Model):
    item_image_id = models.AutoField(primary_key=True)
    item_image = models.ImageField(upload_to='images')
    item = models.ForeignKey(Items, on_delete=None)

    def __str__(self):
        return "{}".format(str(self.item))


class UserAccount(models.Model):
    user_email = models.CharField(max_length=200, primary_key=True)
    contact_regex = RegexValidator(regex=r'^\+?1?\d{8,12}$',
                                   message="Phone number must be entered in the format: '+96565624892'. Up to 12 digits allowed")
    user_contact_number = models.CharField(validators=[contact_regex], blank=False, max_length=12)

    def __str__(self):
        return "{}".format(self.user_email + " " + self.user_contact_number)


class UserAddresses(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=500)
    contact_regex = RegexValidator(regex=r'^\+?1?\d{8,12}$',
                                   message="Phone number must be entered in the format: '+96565624892 or 65624892'. Up to 12 digits allowed")
    user_contact_number = models.CharField(validators=[contact_regex], blank=False, max_length=12)
    user_area = models.CharField(max_length=200)
    user_block = models.CharField(max_length=200)
    user_street = models.CharField(max_length=200)
    user_jedda = models.CharField(max_length=100)
    user_house = models.CharField(max_length=200)
    user_floor = models.CharField(max_length=200)
    user_other_contact_info = models.CharField(max_length=200)
    user_email = models.ForeignKey(UserAccount, on_delete=None)

    def __str__(self):
        return "{}".format(str(self.address_id) + " - " + self.user_email.user_email)


class CartItems(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Items, on_delete=None)
    item_quantity = models.IntegerField()
    item_size = models.FloatField(default=None, blank=True, null=True)
    item_size_type = models.CharField(max_length=20, default=None, blank=True, null=True)
    user_email = models.ForeignKey(UserAccount, on_delete=None)

    def __str__(self):
        return "{}".format(str(self.item) + " " + str(self.item_quantity) + " " + str(self.user_email))

    @property
    def item_name(self):
        print (self.item.item_name)
        return self.item.item_name

    @property
    def item_price(self):
        return self.item.item_price

    @property
    def item_weight(self):
        return self.item.item_weight

    @property
    def item_type(self):
        return self.item.item_type

    @property
    def item_carat(self):
        return self.item.item_carat

    @property
    def item_color(self):
        return self.item.item_color

    @property
    def item_image(self):
        return self.item.item_image.url


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    delivery_address = models.ForeignKey(UserAddresses, on_delete=None)

    def __str__(self):
        return "{}".format(str(self.order_id) + " " + str(self.delivery_address))

    @property
    def user_contact_number(self):
        return self.delivery_address.user_contact_number

    @property
    def user_area(self):
        return self.delivery_address.user_area

    @property
    def user_block(self):
        return self.delivery_address.user_block

    @property
    def user_street(self):
        return self.delivery_address.user_street

    @property
    def user_jedda(self):
        return self.delivery_address.user_jedda

    @property
    def user_house(self):
        return self.delivery_address.user_house

    @property
    def user_floor(self):
        return self.delivery_address.user_floor


class OrderedItem(models.Model):
    ordered_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Items, on_delete=None)
    item_quantity = models.IntegerField()
    item_size = models.FloatField(default=None, blank=True, null=True)
    item_size_type = models.CharField(max_length=20, default=None, blank=True, null=True)
    user_email = models.ForeignKey(UserAccount, on_delete=None)
    order_date = models.CharField(max_length=20)
    order_status = models.CharField(max_length=30,default="Processing")
    order_id = models.ForeignKey(Orders, on_delete=None)
    user_description = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(str(self.item) + "-" + str(self.item_quantity) + " - " + str(self.user_email))

    #@property
    #def item_id(self):
    #    return self.item.item_id

    @property
    def item_name(self):
        return self.item.item_name

    @property
    def item_weight(self):
        return self.item.item_weight

    @property
    def item_price(self):
        return self.item.item_price

    @property
    def item_image(self):
        return self.item.item_image.url if self.item.item_image else ''

    @property
    def item_type(self):
        return self.item.item_type
