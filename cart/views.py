import re
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm, OrderSave
from .models import Order, OrderItem


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    # Получить сессию 'cart'
    # sv = (request.session.get('cart'))
    # print(sv)

    massiv3 = []

    for item in cart:
        massiv1 = []
        # print('======================='),
        ts = item['product'],
        # Перевод получаемого айди в integer, numbers[0]
        numbers = re.findall(r'\b\d+\b', (str(ts)))
        cenazatovar = item['price']
        # print('Цена за шт',cenazatovar)
        kolvo = item['quantity']
        # print('Кол-во приобретаемого товара', cenazatovar)
        total_item = item['price'] * item['quantity']
        # print('Итоговая сумма товара', total_item)
        product_poisk = Product.objects.filter(id=(int(numbers[0])))
        # Перебор массива для вывода получаемых данных
        for person in product_poisk:
            nametovar = [person.name]

        # Запись всех данных в список
        massiv1.append(nametovar[0])
        massiv1.append(int(cenazatovar))
        massiv1.append(int(kolvo))
        massiv1.append(int(total_item))

        # Запись списка в другой список
        massiv3.append(massiv1)

    # print(massiv3)

    form = OrderSave()

    if request.method == "POST":
        form = OrderSave(request.POST)
        if form.is_valid():
            unicn = random.uniform(0, 100)
            number = request.POST.get("number")
            adres2 = request.POST.get("adres")
            message2 = request.POST.get("message")
            priceorder = request.POST.get("price")

            element = Order(number=number, address=adres2, message=message2, price=str(priceorder) + ' ₽',
                            unicnum=unicn, status='N')
            element.save()

            for sv in massiv3:
                name = sv[0]
                price_van_tovar = str(sv[1]) + ' ₽'
                kolvotovara = sv[2]
                priceall = str(sv[3]) + ' ₽'
                element = OrderItem(product=name, price_1_product=price_van_tovar, quantity=kolvotovara,
                                    price_all=priceall, id_order=unicn)
                element.save()

            cart.clear()
            massiv3.clear()
            return HttpResponseRedirect('/cart/order-sent-successfully/')


        else:
            form = OrderSave()

    massiv3.clear()

    # Генерация случайного числа от 0 до 100 (0.9239781787291634)
    # print(random.uniform(0, 100))
    return render(request, 'cart/korzina.html', {'cart': cart, 'form': form, })


def ordersentsuccessfully(request):
    return render(request, "cart/ordersentsuccessfully.html")