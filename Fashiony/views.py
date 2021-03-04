from django.shortcuts import render,redirect



# Create your views here.




def Index(request):
    return render(request, 'Index.html')

def Products(request):
    return render(request, 'Products.html')

def Product_Details(request):
    return render(request, 'Product_Details.html')

def Cart(request):
    return render(request, 'Cart.html')

def Account(request):
    return render(request, 'Account.html')
