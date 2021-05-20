from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.decorators.http import require_POST
import requests
import json

from movies.models import Movie
from .cart import Cart
from .forms import AddToCartForm, OrderDetailForm
from .models import OrderItem


def cart_detail(request):
    cart = Cart(request)
    form = AddToCartForm()
    data=requests.get('https://www.nbrb.by/api/exrates/rates/145')
    currencies_usd=json.loads(data.text)
    context = {'cart': cart, 'form': form, 'currencies_usd': currencies_usd}
    return render(request, 'cart_detail.html', context)


@require_POST
def add_cart(request, id):
    cart = Cart(request)
    product = get_object_or_404(Movie, id=id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cart.add(product=product, quantity=form.cleaned_data.get('quantity', 1))
    return redirect('cart:cart_detail')


# @require_POST
def remove_item(request, id):
    cart = Cart(request)
    product = get_object_or_404(Movie, id=id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def order_form(request):
    data=requests.get('https://www.nbrb.by/api/exrates/rates/145')
    currencies_usd=json.loads(data.text)
    # cart = Cart(request)
    # form = AddToCartForm()
    # form_order = OrderDetailForm()
    # context = {'cart': cart, 'form': form, 'form_order': form_order}
    # if request.method=='POST':
    #     form_order = OrderDetailForm(request.POST)
    #     if form_order.is_valid():
    #         order = form_order.save()
    #         save_orderitem(request, order)
    #         Cart.clear()
    #     else:
    #         context['form_order']=form_order
    #
    # return render(request, 'order_form.html',context)
    cart = Cart(request)
    context = {'order_form': OrderDetailForm(), 'cart': cart, 'currencies_usd':currencies_usd}
    if request.method == "POST":
        form = OrderDetailForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, price=item['price'], product=item['product'],
                                         quantity=item['quantity'])
            cart.clear()
            context['order'] = order
            # del context['order_form']
            return render(request, 'check.html', context)
        else:
            context['order_form'] = form
    return render(request, 'order_form.html', context)


def save_orderitem(request, order):
    for item in Cart(request):
        OrderItem.objects.create(order=order, price=item['price'], product=item['product'], quantity=item['quantity'])
