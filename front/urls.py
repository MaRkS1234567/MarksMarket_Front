from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='home'),
    path('adjustments', views.adjustments, name='adjustments'),
    path('about-us', views.about, name='about'),
    path('login', views.signin, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.signout, name='logout'),
    path('help', views.help_view, name='help'),
    path('account', views.account, name='account'),
    path('note', views.note, name='note'),
    path('chats', views.chats, name='chats'),
    path('favorites', views.favourites, name='favorites'),
    path('my_products', views.my_products, name='my_products'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('news', views.news, name='news'),
    path('product', views.product, name='product'),
    path('yields', views.yields , name='yields'),
    path('order', views.order , name='order'),
    path('profile', views.profile, name='profile'),
    path('favorite', views.favorite, name='favorite'),
    path('favorite_for_yields', views.favorite_for_yields, name='favorite_for_yields'),
    path('chat', views.chat, name='chat'), 
    path('product-update', views.productUpdateView , name='product-update'),
    path('product-delete', views.productDeleteView , name='product-delete'),
    path('user-delete', views.userDeleteView , name='user-delete'),
    path('favorite-delete', views.favoriteDeleteView , name='favorite-delete'),
    path('order-update', views.orderUpdateView , name='order-update'),
    path('order-delete', views.orderDeleteView, name='order-delete')
]
