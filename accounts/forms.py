from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import UserProfile


class RegistationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

        def save(self, commit = True):
            user = super(RegistationForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user



class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User

        fields = (
            'email',
            'first_name',
            'last_name',
        )
        exclude = ()


class EditProfileForm2(forms.ModelForm):

     class Meta:
         model = UserProfile

         fields = (
             'description',
             'city',
             'website',
             'phone',
             'image'
         )
         exclude = ()

