from django import forms
from .models import Category, Product, Cart

class FormCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('description')
        widgets = {
            'description': forms.TextInput(attrs={'class': 'pub_description'}),
        }

class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('titulo', 'imagen', 'description','price', 'category')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
            'imagen': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'pub_imagen'}),
            'description': forms.TextInput(attrs={'class': 'pub_description'}),
            'price': forms.Textarea(attrs={'class': 'pub_price'}),
        }
        
class FormCart(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('usuario', 'product', 'total')
        widgets = {
            'total': forms.Textarea(attrs={'class': 'pub_total'}),
        }