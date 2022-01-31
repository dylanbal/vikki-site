from django.forms import ModelForm
from .models import Customer, ALL_OPTIONS

class BasicForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"