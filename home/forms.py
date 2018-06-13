from django import forms
from home.models import Post


class HomeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write job title...'
        }
    ))

    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write job description...'
        }
    ))

    salary = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': '$0 - $999,999'
        }
    ))

    location = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write job location...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post','title','salary','location',)              #tuple unpacking ignored

