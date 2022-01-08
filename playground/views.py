from django.db.models.expressions import OrderBy
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Max, Min, Avg, Sum, Count
from store.models import Collection, Customer, Product, OrderItem, Order




def say_hello(request):
    
    queryset = Product.objects.annotate(total_amount=Sum(
        F('orderitem__unit_price') * F('orderitem__quantity')
        )).order_by('-total_amount')[:5]
    
    return render(request, 'hello.html', {'name': 'Sher', 'result': list(queryset)})


def home_page(request):
    return HttpResponse('<h1>Home Page</h1>') 
