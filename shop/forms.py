from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    full_name = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()
    country = CountryField(blank_label='(select country)').formfield(
    widget=CountrySelectWidget(attrs={
    'class': 'custom-select d-block w-100',
    }))
    city = forms.CharField()
    street = forms.CharField()
    building = forms.CharField()
    appartment = forms.CharField()
    zip = forms.CharField()

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
