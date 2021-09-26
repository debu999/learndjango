from django import forms
from django.forms import ModelForm, Form

from products.models import Product


class ProductForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title for the Product"}))  # label
    featured = forms.BooleanField(required=False)

    class Meta:
        model = Product
        fields = ["title", "description", "price", "summary", "featured"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "P_" in title:
            return title
        else:
            raise forms.ValidationError(f"Title should have P_ please check and rectify...")


class RawProductForm(Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title for the Product"}))  # label
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()
    summary = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "new-class-name two",
               "rows": 6,
               "cols": 10,
               "id": "dummytextarea",
               "placeholder": "Descriptions for the Product"}))
    featured = forms.BooleanField(required=False)
