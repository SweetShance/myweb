from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label="用户名", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '输入用户名'}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '输入密码'}))