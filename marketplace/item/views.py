from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm

@login_required
def create_item(request):
    """
    Permite a un usuario registrado crear un producto.
    """
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user  # asigna automáticamente al usuario
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item/create_item.html', {'form': form})

def item_list(request):
    """
    Lista todos los productos disponibles.
    """
    items = Item.objects.all()

    # Solo USD
    for item in items:
        item.converted_price = item.price

    context = {
        'items': items,
        'current_currency': 'USD',
    }
    return render(request, 'item/item_list.html', context)





