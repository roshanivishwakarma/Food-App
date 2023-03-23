from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import item
# import requests

# Create your views here.
def index(request):
    food=item.objects.all()
    context={
        'food':food
    }
    # return HttpResponse("food page", context)
    return render(request, 'index.html', context)
def add_item(request):
    if request.method=='POST':
        form = item
        form.item_name=request.POST['item_name']
        form.item_desc=request.POST['item_desc']
        form.item_price=request.POST['item_price']
        form.item_image=request.POST['item_image']
        form.save
        return redirect(request,('index'))
    return render(request, 'add.html/')

def delete_item(request, item_id):
    items=item.objects.get(pk=item_id)
    if request.method=='POST':
        items.delete()
        return redirect('index')
    return render(request,'delete.html/',{'items':items})