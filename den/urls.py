from django.contrib import admin
from django.urls import path, re_path, include

from shop import views

from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
     path('admin/', admin.site.urls),
#Сайты
     path('', views.index, name='main'),
     path('delivery', views.page_dostavka, name='delivery'),
     path('catalog/', views.catalog, name='catalog'),
     path('catalog/<str:slug_name>/', views.category_products, name='category_products'),


     path('send-message/', views.send_message, name='send-message'),
     path('message-done/', views.message_done, name='message-done'),
     # path('test2/', views.test2),

     re_path(r'^cart/', include(('cart.urls', 'cart'), namespace='cart'), name='cart'),
     # path('korzina', views.korzina, name='korzina'),
     # re_path(r'^', include(('shop.urls', 'shop'), namespace='shop')),


#Регистрация и авторизация
     path('registration/', views.registration, name='reg'),
     path('login/', views.LoginUser.as_view(), name='login'),
     path('catalog/successfully', views.success, name='success'),
     path('logout/', views.logout_view, name='logout'),

#Вывод одного товара на сайт
     path('catalog/products/<str:slug_tovar>/', views.products_product, name='catalog_tv2'),
]


# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)