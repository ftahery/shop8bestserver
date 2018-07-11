from rest_framework import serializers
from .models import UserAccount,Items,CartItems,Orders,ItemImages,UserAddresses,OrderedItem


class ItemListSerializer(serializers.ModelSerializer):

    item_image = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ('item_id', 'item_name', 'item_color', 'item_carat',
                  'item_price', 'item_weight','item_type', 'item_quantity',
                  'item_image')

    def get_item_image(self, instance):
        # returning image url if there is an image else blank string
        return instance.item_image.url if instance.item_image else ''


class OrderListSerializer(serializers.ModelSerializer):

    user_building_details = serializers.CharField(source='delivery_address.user_building_details')
    user_street_details = serializers.CharField(source='delivery_address.user_street_details')
    user_country = serializers.CharField(source='delivery_address.user_country')
    user_area = serializers.CharField(source='delivery_address.user_area')

    class Meta:
        model = Orders
        fields = ('order_id','user_contact_number','user_building_details','user_street_details','user_country','user_area')


class OrderedItemListSerilizer(serializers.ModelSerializer):

    item_id = serializers.IntegerField(source='item.item_id')
    item_name = serializers.CharField(source='item.item_name')
    item_price = serializers.DecimalField(source='item.item_price',max_digits=5,decimal_places=2)
    item_image = serializers.ImageField(source='item.item_image')
    item_weight = serializers.DecimalField(source='item.item_weight',max_digits=10, decimal_places=5)
    item_type =  serializers.CharField(source='item.item_type')

    class Meta:
        model = OrderedItem
        fields = ('item_id','item_name','item_price','item_weight','item_size',
                  'item_size_type','item_type','item_image','item_quantity',
                  'order_status','order_date')


class UserAccountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ('user_email', 'user_id', 'user_contact_number')


class CartItemsListSerializer(serializers.ModelSerializer):

    item_id = serializers.IntegerField(source='cart_item.item_id')
    item_name = serializers.CharField(source='cart_item.item_name')
    item_price = serializers.DecimalField(source='cart_item.item_price',max_digits=5, decimal_places=2)
    item_carat = serializers.IntegerField(source='cart_item.item_carat')
    item_color = serializers.CharField(source='cart_item.item_color')
    item_image = serializers.ImageField(source='cart_item.item_image')
    item_weight = serializers.DecimalField(source='cart_item.item_weight',max_digits=10, decimal_places=5)
    item_type = serializers.CharField(source='cart_item.item_type')
    user_email = serializers.CharField(source='user_email.user_email')

    class Meta:
        model = CartItems
        fields = ('item_id','item_quantity', 'item_name', 'item_price', 'item_weight',
                  'item_size', 'item_size_type','item_type', 'item_carat', 'item_color',
                  'item_image', 'user_email')

    def get_item_image(self,instance):
        return instance.item_image.url if instance.item_image else ''


class ItemImagesListSerializer(serializers.ModelSerializer):
    item_image = serializers.SerializerMethodField()
    item = serializers.SerializerMethodField()

    class Meta:
        model = ItemImages
        fields = ('item_image','item')

    def get_item_image(self, instance):
        # returning image url if there is an image else blank string
        return instance.item_image.url if instance.item_image else ''

    def get_item(self,instance):
        return instance.item.item_id if instance.item_image else ''


class UserAddressesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddresses
        fields = ('address_id','user_name','user_contact_number','user_building_details',
                  'user_street_details','user_pincode','user_country','user_area','user_email')



