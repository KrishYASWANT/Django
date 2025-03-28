from django.shortcuts import get_object_or_404, render
from store.models import  Product
from .cart import Cart
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
def cart_summary(request): 
    return render(request, 'cart_summary.html', {}) 
def cart_add(request): 
    #Get the cart 
    cart= Cart(request) 
    # test for POST 
    if request.POST.get('action') == 'post': 
        # Get stuff 
        product_id= int(request.POST.get('product_id')) 
        #lookup product in DB 
        product = get_object_or_404(Product, id=product_id)
        # Save Session
        cart.add(product=product)
        # Get Cart Quantity
        cart_quantity = cart.__len__()
        
        # Return Response
        # response  = JsonResponse({'Product Name: ':product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response
def cart_delete(request): 
    pass 
def cart_update (request): 
    pass