from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label="Количество:",max_value=20)
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int,label="Количество:")
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderSave(forms.Form):
    number = forms.IntegerField(label="Ваш номер телефона")
    adres = forms.CharField(max_length=200, label="Адрес доставки (город, улица, квартира)")
    message = forms.CharField(max_length=500, required=False, label="Сообщение (не обязательное поле)")



