from django import forms 

class ProductForm(forms.Form):
    user_image = forms.FileField()