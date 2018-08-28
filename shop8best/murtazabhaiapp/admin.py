# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ItemImages,UserAddresses,UserAccount,CartItems,Items,Orders,OrderedItem

# Register your models here.

admin.site.register(Items)
admin.site.register(ItemImages)
admin.site.register(UserAddresses)
admin.site.register(UserAccount)
admin.site.register(CartItems)
admin.site.register(Orders)
admin.site.register(OrderedItem)


