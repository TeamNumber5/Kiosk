from django import forms

class SubmitLogin(forms.Form):
    user_name = forms.CharField(label='user_name', max_length=100)
    user_password = forms.CharField(label='user_password',max_length=100)

