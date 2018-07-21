from django.conf.urls import url
from .views import ItemListView,OrderListView,CartItemsListView,UserAccountListView,ItemImagesListView,\
    UserAddressesListView,CartCountAPIView,IsCartItemPresent,AddItemToCart,RemoveItemFromCart,AddQuantityToCartItem,\
    MinusQuantityFromCartItem,DeleteUserAddress,UpdateUserAddress,RetrieveUserAddress,PlaceOrder,OrderedListView,\
    SendEmail,DeleteEverythingFromOrder,CreateUser,ItemByTypeListView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns=[
    url(r'^getItems/$',ItemListView.as_view(),name='itemsList'),
    url(r'^getOrders/$', OrderListView.as_view(), name='orderList'),
    url(r'^getCartItems/$', CartItemsListView.as_view(), name='cartItemsList'),
    url(r'^getUsers/$', UserAccountListView.as_view(), name='usersList'),
    url(r'^getImages/$', ItemImagesListView.as_view(),name='itemImages'),
    url(r'^getUserAddresses/$',UserAddressesListView.as_view(),name='userAddresses'),
    url(r'^deleteUserAddress/(?P<address_id>\d+)/$',DeleteUserAddress.as_view(),name='deleteUserAddress'),
    url(r'^updateUserAddress/$',UpdateUserAddress.as_view(),name='updateAddress'),
    url(r'^getUserAddress/(?P<address_id>\d+)/$', RetrieveUserAddress.as_view(), name='getUserAddress'),
    url(r'^getCartCount/$',CartCountAPIView.as_view(),name='cartCount'),
    url(r'^isCartItem/item_id/(?P<item_id>\d+)/$',IsCartItemPresent.as_view(),name='isCartItem'),
    url(r'^addItemToCart/$',AddItemToCart.as_view(),name="addItemToCart"),
    url(r'^removeItemFromCart/item_id/(?P<item_id>\d+)/$',RemoveItemFromCart.as_view(),name="removeItemFromCart"),
    url(r'^addQuantityToCartItem/item_id/(?P<item_id>\d+)/quantity/(?P<quantity>\d+)/$',AddQuantityToCartItem.as_view(),name='addQuantityToCartItem'),
    url(r'^minusQuantityFromCartItem/item_id/(?P<item_id>\d+)/$',MinusQuantityFromCartItem.as_view(),name='minusQuantityFromCartItem'),
    url(r'^placeOrder/$',PlaceOrder.as_view(),name='placeOrder'),
    url(r'^getPastOrders/$',OrderedListView.as_view(),name='getPastOrders'),
    url(r'^sendEmail/$',SendEmail.as_view(),name='sendEmail'),
    url(r'^deleteOrders/$',DeleteEverythingFromOrder.as_view(),name='deleteOrders'),
    url(r'^createUser/$',CreateUser.as_view(),name='createUser'),
    url(r'^getItemByType/item_type/(?P<item_type>\D+)/$',ItemByTypeListView.as_view(),name='getItemByType'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
