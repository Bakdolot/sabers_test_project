from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Article


class ArticleForm(forms.ModelForm):
    images = forms.ImageField(
        label=_("images"), widget=forms.ClearableFileInput(attrs={"multiple": True})
    )

    class Meta:
        model = Article
        fields = "__all__"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["short_description"].required = False
