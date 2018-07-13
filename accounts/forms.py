from django import forms
from django.contrib.auth.forms import UserCreationForm
from super_polls.models import User_Polls, User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SignUpPollsForm(forms.ModelForm): 
    class Meta:
        model = User_Polls
        fields = ('security_question', 'security_answer')