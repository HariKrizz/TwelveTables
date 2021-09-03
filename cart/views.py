from django.core.checks import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.sessions.models import Session
from .models import *
from shop.models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_details(request, total=0, count=0, c_items=None):
    try:   
        crt_lst = cartList.objects.get(cart_id=crt_id(request))   #here (same in context_processor)
        c_items = itemsCart.objects.filter(cart=crt_lst, active=True)

        for i in c_items:
            total += (i.prod.price * i.qty)
            count += i.qty
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html', {'c_items':c_items, 'c_tot':total, 'count':count})

def crt_id(request):
    c_id = request.session.session_key
    if not c_id:
        c_id = request.session.create
    return c_id
    
def add_cart(request,prdct_id):
    product = Product.objects.get(id=prdct_id)
    
    try:
        crt_lst = cartList.objects.get(cart_id=crt_id(request))      # ----> user=request.user
    except cartList.DoesNotExist:
        crt_lst = cartList.objects.create(cart_id=crt_id(request))
        crt_lst.save()
    
    try:
        crt_items = itemsCart.objects.get(prod=product,cart=crt_lst)
        if crt_items.qty < crt_items.prod.stock:
            crt_items.qty += 1
        crt_items.save()
    except itemsCart.DoesNotExist:
        crt_items = itemsCart.objects.create(prod=product,qty=1,cart=crt_lst)
        crt_items.save()
        
    return redirect('cart_details')

def decrement_cart(request,prdct_id):
    ct_item = cartList.objects.get(cart_id=crt_id(request))   #here also
    prodct = get_object_or_404(Product,id=prdct_id)
    cart_items = itemsCart.objects.get(prod=prodct,cart=ct_item)

    if cart_items.qty > 1:
        cart_items.qty -= 1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cart_details')

def delete_cart(request,prdct_id):
    ct_item = cartList.objects.get(cart_id=crt_id(request))   #here
    prodct = get_object_or_404(Product,id=prdct_id)
    cart_items = itemsCart.objects.get(prod=prodct,cart=ct_item)
    cart_items.delete()
    return redirect('cart_details')
