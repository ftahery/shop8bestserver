from rest_framework import serializers
from .models import UserAccount, Items, CartItems, Orders, ItemImages, UserAddresses, OrderedItem


class ItemListSerializer(serializers.ModelSerializer):
    item_image = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ('item_id', 'item_name', 'item_color', 'item_carat',
                  'item_price', 'item_weight', 'item_type', 'item_quantity',
                  'item_image')

    def get_item_image(self, instance):
        # returning image url if there is an image else blank string
        return instance.item_image.url if instance.item_image else ''


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = (
            'order_id', 'user_contact_number', 'user_area', 'user_block', 'user_street', 'user_jedda', 'user_house',
            'user_floor')


class OrderedItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = ('item_id', 'item_name', 'item_price', 'item_weight', 'item_size',
                  'item_size_type', 'item_type', 'item_image', 'item_quantity',
                  'order_status', 'order_date')


class UserAccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('user_email', 'user_id', 'user_contact_number')


class CartItemsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ('item_id', 'item_quantity', 'item_name', 'item_price', 'item_weight',
                  'item_size', 'item_size_type', 'item_type', 'item_carat', 'item_color',
                  'item_image', 'user_email')


class ItemImagesListSerializer(serializers.ModelSerializer):
    item_image = serializers.SerializerMethodField()

    class Meta:
        model = ItemImages
        fields = ('item_image', 'item_id')

    def get_item_image(self, instance):
        # returning image url if there is an image else blank string
        return instance.item_image.url if instance.item_image else ''

    def get_item_id(self, instance):
        return instance.item.item_id


class UserAddressesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddresses
        fields = ('address_id', 'user_name', 'user_contact_number', 'user_area',
                  'user_block', 'user_street', 'user_jedda', 'user_house', 'user_floor')
