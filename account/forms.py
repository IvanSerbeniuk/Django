
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(User):

    class Meta:

        model = User 
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs): #to make use of var model and fields above
        super(CreateUserForm, self).__init__(*args, **kwargs)


    # Email validation
    def clean_email(self):

        email = self.clean_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('this email is invalid')

        if len(email >= 150):
            raise forms.ValidationError('Your email is too long')





