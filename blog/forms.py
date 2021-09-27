from django import forms
from django.forms import ModelForm

from blog.models import Article


class ArticleModelForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title for the Article"}))  # label
    active = forms.BooleanField(required=False)

    class Meta:
        model = Article
        fields = ["title", "content", "active"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "A_" in title:
            return title
        else:
            raise forms.ValidationError(f"Title should have A_ please check and rectify...")
