from django.shortcuts import render
from .models import ShippingAddress

def checkout(request):

    # Users with account -- Pre-fill the form
    if request.user.is_authenticated: #if user login

        try:
            # Authinticated users WITH shippping info
            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = {'shipping': shipping_address}

            return render(request, 'payment/checkout.html', context=context)

        except:
            # Authenticated user without shipping info
            return render(request, 'payment/checkout.html')
    
    else: # Можно и без else :)
        # Guest users
        return render(request, 'payment/checkout.html')




def payment_success(request):

    return render(request, 'payment/payment-success.html')

def payment_failed(request):

    return render(request, 'payment/payment-failed.html')