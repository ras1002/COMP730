from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Fund

class SignupForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    username = forms.CharField(label='Username')
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label="Reenter Password")
    email = forms.EmailField(label='Email Address', required=False)


    #set the order of fields
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field_name == 'first_name' or field_name == 'last_name' :
                print(field.label)
                field.widget = forms.TextInput(attrs={'placeholder':field.label})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('This email is already in use')
        return email

    def signup(self, request, user, commit=True):
        user.password = make_password(self.cleaned_data['password1'])
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        f = Fund(owner=user)
        f.save()
        user.save()
        return user

class DepositForm(forms.Form):
    '''
    Used to handle deposits to a user's account
    '''
    amount = forms.DecimalField(max_value=100, min_value=0, max_digits=5, decimal_places=2,required=True)
    date = forms.DateField(required=True)
    comment = forms.CharField(max_length=255, required=True)
