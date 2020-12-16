from django import forms
from .models import Item

class ItemForm(forms.Form):
    
    class Meta:
        model = Item
        fields = ('title', 'author', 'publish')

#new
class SearchForm(forms.Form):
    search_key = forms.CharField(
        label='',
        max_length=128,
        widget = forms.TextInput(attrs={"class": 'float-right', 'placeholder': 'Search...'}),required=False)