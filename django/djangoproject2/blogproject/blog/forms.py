from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta: #meta class
        model = Blog
        fields = ['title','writer','body','image'] #이름표 역할
        