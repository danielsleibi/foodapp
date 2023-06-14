from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'food/index.html', context)


def details(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        # raise an exception "page not found"
        context = {'item_id': item_id}
        return render(request, 'food/error.html', context)
    context = {'item': item}
    return render(request, 'food/details.html', context)


def create_item(request):
    form = ItemForm(request.POST or None)
    form.instance.user = request.user

    if form.is_valid():
        form.save()
        return redirect('food:food')
    return render(request, 'food/item-form.html', {'form': form})


def update_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        # raise an exception "page not found"
        context = {'item_id': item_id}
        return render(request, 'food/error.html', context)

    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:food')
    return render(request, 'food/item-form.html', {'form': form})


def delete_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        # raise an exception "page not found"
        context = {'item_id': item_id}
        return render(request, 'food/error.html', context)
    if request.method == 'POST':
        item.delete()
        return redirect('food:food')
    return render(request, 'food/item-delete.html', {'item': item})
