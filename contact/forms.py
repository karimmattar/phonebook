from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from phonenumber_field.formfields import PhoneNumberField

from .models import ContactNumber


class ContactNumberForm(forms.ModelForm):
    """
    Contact number form.
    """

    number = PhoneNumberField(region='EG')
    label = forms.ChoiceField(choices=ContactNumber.LABELS, initial='other')

    class Meta:
        model = ContactNumber
        fields = ['label', 'number', 'contact']
        extra_kwargs = {'contact': {'read_only': True}}
