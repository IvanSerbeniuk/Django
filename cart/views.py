from django.shortcuts import render

from .cart import Cart #need to check our session

from store.models import Product

from django.shortcuts import get_object_or_404

from django.http import JsonResponse

def cart_summory(request): # obtain session data and pass it on through out cart-summory.html(page)

    cart = Cart(request)
    
    return render(request, 'cart-summary.html', {'cart':cart})


def cart_add(request):

    cart = Cart(request) #we are making use of session class cart()

    if request.POST.get('action') == 'post': #Ошибка капиталайз Пост

        product_id = int(request.POST.get('product_id'))

        product_quantity = int(request.POST.get('product_quantity'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, product_qty=product_quantity)
        
        cart_quantity = cart.__len__()
        
        response = JsonResponse({'qty': cart_quantity})

        return response

def cart_delete(request):

    pass


def cart_update(request):

    pass
