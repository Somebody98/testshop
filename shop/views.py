import json, re, ast
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product, Svyaz
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from .forms import LoginUserForm, RegForm, UserForm

#korzina
from cart.forms import CartAddProductForm



def index(request):
    tovars = Product.objects.filter(id__in=[5, 27, 38, 51])

    context = {
        'pr': tovars,
    }
    return render(request, 'index.html', context)


def page_dostavka(request):
    return render(request, "dostavka.html")


def catalog(request):
    tovar = Category.objects.all().order_by('id')
    tv = {
        'tv': tovar,
    }

    return render(request, "katalog.html", tv)

def category_products(request, slug_name):
    category_poisk = Category.objects.filter(slug=slug_name)
    for person in category_poisk:
        id_cat = person.id
        tovars = Product.objects.filter(category=id_cat)




    context = {
        'pr': tovars,
    }

    return render(request, "tovari.html", context)


# Вывод отдельного товара на страничку html
def products_product(request, slug_tovar):
    product_poisk = Product.objects.filter(slug=slug_tovar)
    for person in product_poisk:
        id_cat = person.id
        tovars = Product.objects.filter(id=id_cat)

    cart_product_form = CartAddProductForm()


    context = {
        'pr': tovars,
        'cart_product_form': cart_product_form,
    }

    return render(request, "opisanietovara.html", context)



# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product/detail.html', {'product': product,
#                                                         'cart_product_form': cart_product_form})


def send_message(request):
    ccurrent_datetime = datetime.now()
    current_datetime = str(ccurrent_datetime)
    print(current_datetime)

    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            message2 = request.POST.get("message")
            number = request.POST.get("number")
            email = request.POST.get("email")
            date = request.POST.get("date")
            element = Svyaz(message=message2, number=number, email=email, datetime=date)
            element.save()

            return HttpResponseRedirect('/message-done/')

        else:
            form = UserForm()
            print('lox')

    context = {
        'form': form, 'current_datetime': current_datetime
    }
    return render(request, "send-message.html", context)

def message_done(request):
    return render(request, "message_done.html")


# Функции авторизации и регистрации
def registration(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'registration_done.html')
    else:
        form = RegForm()
    return render(request, 'reg.html', {'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('success')


# Успешная авторизация
def success(request):
    html = redirect('/catalog')
    html.set_cookie('authorization', 'successful authorization', max_age=None)
    stt = request.COOKIES.get('authorization')
    print(stt)
    return html


# Выход из аккаунта
def logout_view(request):
    logout(request)

    html = redirect('/catalog')
    html.delete_cookie("authorization")
    return html





    # Перебор массива и передача его в (массив - python)
    # test3 = ['1','10','6']
    # people = product.objects.filter(id__in=test3).order_by('id')
    #
    # for person2 in people:
        # print(f"{person2.id} {person2.name} {person2.price}")
        # test2 = [person2.id, person2.name, person2.price]
        # print(test2)



    # Перебор массива для вывода получаемых данных
    # for person in people:
    #     print(f"{person.id}.{person.name} - {person.age}")


    # Вывод данных с 1 по 12 айди
    # people = productinformation.objects.filter(id__range=(1, 12))