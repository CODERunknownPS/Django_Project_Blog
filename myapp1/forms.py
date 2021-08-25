from django import forms
from . models import my_blog


class Edit_Blog(forms.ModelForm):

    class Meta:
        model = my_blog
        fields = ('img', 'title', 'sub_title', 'dsc')
