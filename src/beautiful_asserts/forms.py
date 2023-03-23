from django import forms
from django.core.exceptions import ValidationError

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title",)

    def clean_title(self):
        title = self.cleaned_data["title"]

        if not title[0].isupper():
            raise ValidationError("Should start with an uppercase letter.")

        if "." in title:
            raise ValidationError("The period sign is not allowed.")

        return title
