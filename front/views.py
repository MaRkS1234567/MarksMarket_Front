from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpRequest, HttpResponse

def shop(request):
    context = {}
    return render(request, 'main/shop.html', context)

def adjustments(request):
    context = {}
    return render(request, 'main/adjustments.html')

def about(request):
    context = {}
    return render(request, 'main/about.html', context)

def signin(request):
    context = {}
    return render(request, 'main/login.html', context)

def register(request):
    context = {}
    return render(request, 'main/register.html', context)

def signout(request):
    context = {}
    return render(request, 'main/logout.html', context)

def help_view(request):
    context = {}
    return render(request, 'main/help.html', context)

def account(request):
    context = {}
    return render(request, 'main/account.html', context)

def chats(request):
    context = {}
    return render(request, 'main/chats.html', context)

def note(request):
    context = {}
    return render(request, 'main/note.html', context)

def favourites(request):
    context = {}
    return render(request, 'main/favorites.html', context)

def my_products(request):
    context = {}
    return render(request, 'main/my_products.html', context)

def my_orders(request):
    context = {}
    return render(request, 'main/my_orders.html', context)

def news(request):
    context = {}
    return render(request, 'main/news.html', context)

def product(request):
    context = {}
    return render(request, 'main/product.html', context)

def yields(request):
    context = {}
    return render(request, 'main/yields.html', context)

def order(request):
    context = {}
    return render(request, 'main/order.html', context)

def profile(request):
    context = {}
    return render(request, 'main/profile.html', context)

def favorite(request):
    context = {}
    return render(request, 'main/favorite.html', context)

def favorite_for_yields(request):
    context = {}
    return render(request, 'main/favorite_for_yields.html', context)

def chat(request):
    context = {}
    return render(request, 'main/chat.html', context)

def productUpdateView(request):
    context = {}
    return render(request, 'main/product-update.html', context)

def productDeleteView(request):
    context = {}
    return render(request, 'main/product-delete.html', context)

def userDeleteView(request):
    context = {}
    return render(request, 'main/user-delete.html', context)

def favoriteDeleteView(request):
    context = {}
    return render(request, 'main/favorite-delete.html', context)

def orderUpdateView(request):
    context = {}
    return render(request, 'main/order-update.html', context)

def orderDeleteView(request):
    context = {}
    return render(request, 'main/order-delete.html', context)

