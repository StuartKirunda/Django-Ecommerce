from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (('MM', 'Mobilemoney'), ('COD', 'CashOnDelivery'))


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Acacia John Babiha'}))
    district = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Kampala'}))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
            'id': 'zip'}))
    zip = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    save_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'form-control',
                           'placeholder': 'Promo Code',
                           'aria-label': 'Receipient\'s username',
                           'aria-description': 'basic-addon2',
                           }))
