from django import forms

class SubmitLogin(forms.Form):
    employee_id = forms.CharField(label='employee_id', max_length=5)
    user_password = forms.CharField(label='user_password',max_length=100)





class CreateUser(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    user_password = forms.CharField(label='user_password',max_length=100)
    employee_id = forms.CharField(label='employee_id', max_length=5)
    role = forms.CharField(label='role', max_length=100)
    

