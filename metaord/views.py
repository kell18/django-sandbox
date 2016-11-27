from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Order


def index(request):
    return render(request, 'metaord/index.html', {})

def orders_list(request):
    orders = Order.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'metaord/orders_list.html', {'orders': orders})

def order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'metaord/order.html', {'order': order})
