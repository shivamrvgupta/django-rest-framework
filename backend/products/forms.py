from curses import meta
from dataclasses import field
from django import forms
from .models import Products

class ProductForm(form.ModelForm):
    class Meta:
        model = Products
        fields =  [
            'title',
            'content',
            'price'
        ]