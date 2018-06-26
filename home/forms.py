from django import forms
from home.models import Post, Apply


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

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if int(salary) > 256000:
            raise forms.ValidationError("Salary should not be larger than 256,000$.")
        elif int(salary) <0:
            raise forms.ValidationError("Salary should be positive.")

        return salary


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('add_on',)
        widgets = {
            'add_on': forms.Textarea(attrs={
                'class': 'form-control ',
                'rows': 4,

            })

        }