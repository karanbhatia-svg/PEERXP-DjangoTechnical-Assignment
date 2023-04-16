from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Expence
from django import forms
from django.forms import ModelForm

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={'type': 'text'}))
        password2 = forms.CharField(label='Password confirmation', widget=forms.TextInput(attrs={'type': 'text'}))
        fields = ['username', 'email','password1','password2', 'is_Admin', 'is_Member']

class ExpenceForm(ModelForm):
    class Meta:
        model = Expence
        fields = ['Name', 'Date_of_Expense', 'Category', 'Description', 'Amount']

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super().__init__(*args, **kwargs)

        def save(self, commit=True):
            instance = super().save(commit=False)
            if self.user:
                instance.Created_by  = self.user
            if commit:
                instance.save()
            return instance
