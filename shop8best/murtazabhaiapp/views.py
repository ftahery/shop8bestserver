# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from rest_framework import generics
from .models import Items,Orders,UserAccount,CartItems,ItemImages,UserAddresses,OrderedItem
from .serializers import ItemListSerializer,OrderListSerializer,CartItemsListSerializer, UserAccountListSerializer,ItemImagesListSerializer,UserAddressesListSerializer,OrderedItemListSerilizer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
import requests
import json
from django.core.mail import send_mail
from django.template import loader

client_id = "827748585652-1huqi76j434rgvavviimlrquutlp9lgh.apps.googleusercontent.com"


def validate_token(self, request):
    authorization_header = request.META.get('HTTP_AUTHORIZATION')
    access_token = authorization_header
    print (access_token)
    response = requests.get("https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=" + access_token)
    data = response.json()
    aud = data['audience']
    return aud


def getEmailandAud(self,request):
    authorization_header = request.META.get('HTTP_AUTHORIZATION')
    access_token = authorization_header
    print (access_token)
    response = requests.get("https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=" + access_token)
    data = response.json()
    aud = data['audience']
    email = data['email']
    return aud,email


class DeleteEverythingFromOrder(APIView):

    def get(self):
        OrderedItem.objects.all().delete()
        return Response("")


class ItemListView(generics.ListCreateAPIView):

    def get(self, request):
        items = Items.objects.all()
        serializer_class = ItemListSerializer(items, many=True)
        return JsonResponse(serializer_class.data,safe = False)

    #def perform_create(self, serializer):
    #   serializer.save()


class OrderListView(generics.ListCreateAPIView):

    def get(self,request):
        aud = validate_token(self,request)

        if aud == client_id:
            orders = Orders.objects.all()
            serializer_class = OrderListSerializer(orders,many=True)
            return JsonResponse(serializer_class.data,safe= False)

        return Response("")


class OrderedListView(generics.ListCreateAPIView):

    def get(self,request,**kwargs):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:

            try:
                ordered_items = OrderedItem.objects.filter(user_email=email)
            except OrderedItem.DoesNotExist:
                ordered_items = None
            serializer_class = OrderedItemListSerilizer(ordered_items,many=True)
            return JsonResponse(serializer_class.data,safe=False)

        return Response("")


class CreateUser(generics.CreateAPIView):

    def get(self,request):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            user = UserAccount(user_email=email)
            user.save()
            return JsonResponse({"message": True})

        print ("Failed to save user" + email)
        return JsonResponse({"message": False})


class PlaceOrder(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):
        aud, email = getEmailandAud(self, request)

        if aud == client_id:
            order_data = json.loads(request.body.decode('utf-8'))
            user = UserAccount.objects.get(user_email=email)
            cart_items = CartItems.objects.filter(user_email=user)

            delivery_address = UserAddresses.objects.get(address_id=order_data['address_id'])
            description = order_data['user_description']
            new_order = Orders(delivery_address=delivery_address)
            new_order.save()

            total_amount = 0.000
            item_prices = []

            for cart_item in cart_items:
                order_item = OrderedItem(item=cart_item.item,item_quantity=cart_item.item_quantity,
                                         item_size=cart_item.item_size,item_size_type=cart_item.item_size_type,
                                         user_email=user,order_id=new_order,order_date=order_data['order_date'], user_description=description,
                                         order_status="Processing")
                total_amount += total_amount + (cart_item.item_quantity * cart_item.item.item_price)
                item_prices.append(cart_item.item_quantity * cart_item.item.item_price)
                order_item.save()

            items_and_prices = zip(cart_items,item_prices)

            context = dict({
                'items_and_prices': items_and_prices,
                'description': description,
                'delivery_address': delivery_address,
                'total_amount': total_amount,
                'delivery_amount': "Will be sent later"
            })
            template = loader.render_to_string('murtazabhaiapp/email_template.html', context)

            send_mail('Order placed successfully',
                      'Thank you for ordering from Shop8Best',
                      'info@shop8best.com',
                      [email, 'murtazatahery110@yahoo.com'],
                      html_message=template,)

            cart_items.delete()

            return JsonResponse({"message":True})

        return Response("")



class CartItemsListView(generics.ListCreateAPIView):

    def get(self, request):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            user = UserAccount.objects.get(user_email=email)
            cart_items = CartItems.objects.filter(user_email=user)
            serializer_class = CartItemsListSerializer(cart_items, many=True)
            return JsonResponse(serializer_class.data,safe=False)

        return Response("")

class UserAccountListView(generics.ListCreateAPIView):

    def get(self,request):
        aud = validate_token(self,request)

        if aud == client_id:
            user_account = UserAccount.objects.all()
            serializer_class = UserAccountListSerializer(user_account, many=True)
            return JsonResponse(serializer_class.data, safe=False)

        return Response("")


class ItemImagesListView(generics.ListCreateAPIView):

    def get(self, request):
        item_images = ItemImages.objects.all()
        serializer_class = ItemImagesListSerializer(item_images, many=True)
        return JsonResponse(serializer_class.data, safe=False)


class UserAddressesListView(generics.ListCreateAPIView):

    def get(self, request):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            user_addresses = UserAddresses.objects.filter(user_email=email)
            serializer_class = UserAddressesListSerializer(user_addresses,many=True)
            return JsonResponse(serializer_class.data, safe=False)

        return Response("")


class DeleteUserAddress(generics.CreateAPIView):

    def get(self,request,**kwargs):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            address_id = kwargs['address_id']
            user_address = UserAddresses.objects.get(address_id=address_id,user_email=email)
            user_address.delete()
            return JsonResponse({"message":"Success"})

        return Response("")


class RetrieveUserAddress(generics.CreateAPIView):

    def get(self,request,**kwargs):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            address_id = kwargs['address_id']
            user_address = UserAddresses.objects.get(address_id=address_id,user_email=email)
            data = serializers.serialize("json",user_address)
            return JsonResponse(data)

        return Response("")



class UpdateUserAddress(generics.CreateAPIView):

    def post(self,request,**kwargs):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            if request.method == 'POST':
                print (request.body)
            data = json.loads(request.body.decode('utf-8'))

            address_id = data['address_id']
            user_name = data['user_name']
            user_contact_number = data['user_contact_number']
            user_area = data['user_area']
            user_block = data['user_block']
            user_street = data['user_street']
            user_jedda = data['user_jedda']
            user_house = data['user_house']
            user_floor = data['user_floor']
            user_other_contact_info = data['user_other_contact_info']

            user_email = UserAccount.objects.get(user_email=email)

            if address_id==0:
                new_address = UserAddresses(user_name=user_name,user_contact_number=user_contact_number,
                                            user_area=user_area, user_block=user_block,
                                            user_street=user_street,user_jedda=user_jedda,
                                            user_house=user_house,user_floor=user_floor,user_other_contact_info=user_other_contact_info,user_email=user_email)
                new_address.save()
                return JsonResponse({"message":"Success","address_id":new_address.address_id})

            update_address = UserAddresses.objects.get(address_id=address_id)
            update_address.user_name = user_name
            update_address.user_contact_number = user_contact_number
            update_address.user_area = user_area
            update_address.user_block = user_block
            update_address.user_street = user_street
            update_address.user_jedda = user_jedda
            update_address.user_house = user_house
            update_address.user_floor = user_floor
            update_address.user_other_contact_info = user_other_contact_info

            update_address.save()
            return JsonResponse({"address_id":update_address.address_id})

        return Response("")


class CartCountAPIView(generics.CreateAPIView):

    def get(self, request):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            user = UserAccount.objects.get(user_email=email)
            cart_items_count = CartItems.objects.filter(user_email=user.user_email).count()
            print (cart_items_count)
            return JsonResponse({email:cart_items_count})

        return Response("")


class IsCartItemPresent(APIView):

    def get(self, request, *args, **kwargs):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            item_id = kwargs.get('item_id')
            items = Items.objects.get(item_id=item_id)
            user = UserAccount.objects.get(user_email=email)
            cart_items_count = CartItems.objects.filter(item=items,user_email=user.user_email).count()

            if(cart_items_count>0):
                return JsonResponse({'message':True})

            return JsonResponse({'message':False})

        return Response("")


class RemoveItemFromCart(APIView):

    def get(self,request,*args,**kwargs):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            item_id = kwargs.get('item_id')
            items = Items.objects.get(item_id=item_id)
            user = UserAccount.objects.get(user_email=email)
            cart_items = CartItems.objects.get(item=items,user_email=user.user_email)
            print (cart_items)
            cart_items.delete()
            return JsonResponse({"message":"Success"})

        return Response("")


class AddItemToCart(APIView):

    def post(self,request):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            if request.method == 'POST':
                print (request.body)
            data = json.loads(request.body.decode('utf-8'))
            item_id = data['item_id']
            item_size = data['item_size']
            item_size_type = data['item_size_type']
            item = Items.objects.get(item_id=item_id)
            item_size = item_size
            item_size_type = item_size_type
            user = UserAccount.objects.get(user_email=email)
            cart_items = CartItems(item=item,item_quantity=1,item_size=item_size,item_size_type=item_size_type,user_email=user)
            print (cart_items)
            cart_items.save(force_insert=True)
            return JsonResponse({"message":"Success"})

        return Response("")


class AddQuantityToCartItem(APIView):

    def get(self,request,*args,**kwargs):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            item_id = kwargs.get('item_id')
            quantity = kwargs.get('quantity')
            items = Items.objects.get(item_id=item_id)
            if int(quantity)+1 > int(items.item_quantity):
                return JsonResponse({"message":False})

            user = UserAccount.objects.get(user_email=email)
            existingCartItem = CartItems.objects.get(item=items,user_email=user.user_email)
            print (existingCartItem)
            existingCartItem.item_quantity+=1
            existingCartItem.save(update_fields=['item_quantity'])
            return JsonResponse({"message":True})


class MinusQuantityFromCartItem(APIView):

    def get(self,request,*args,**kwargs):
        aud,email = getEmailandAud(self,request)

        if aud == client_id:
            item_id = kwargs.get('item_id')
            items = Items.objects.get(item_id=item_id)
            user = UserAccount.objects.get(user_email=email)
            cart_items = CartItems.objects.get(item=items, user_email=user.user_email)
            cart_items.item_quantity-=1
            cart_items.save(update_fields=['item_quantity'])
            return JsonResponse({"message":True})

        return JsonResponse({"message":False})


class ItemByTypeListView(generics.ListCreateAPIView):

    def get(self,request,**kwargs):
        item_type = kwargs.get('item_type')
        items = Items.objects.filter(item_type=item_type)

        for item in items:
            print (item.item_type)

        serializer_class = ItemListSerializer(items, many=True)
        return JsonResponse(serializer_class.data, safe=False)


class SendEmail(APIView):

    def get(self,request,*args,**kwargs):
        send_mail('something','Hi Fakhruddin','info@shop8best.com',['info@shop8best.com'])

        return Response("")





