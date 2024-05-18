from django.forms import forms
from .models import Post

class FormPost(forms.ModelForm):   
    class Meta:
        model = Post
        fields = ("__all__")
